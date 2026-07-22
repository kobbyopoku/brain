---
title: "AgenticRAG: Letting LLMs Hunt for Evidence. Here's the Full Agentic Upgrade"
source: https://x.com/beamnxw/status/2079523981363692005
author:
  - "[[@beamnxw]]"
published: 2026-07-21
created: 2026-07-22
description: "I think you know that most RAG systems still work like this: ask a question, grab some chunks, stuff them into a prompt, and prayOne shot. N..."
tags:
  - "clippings"
  - "agent-memory"
  - "rag"
  - "agentic-engineering"
---
![Image](https://pbs.twimg.com/media/HNtCPqWWcAA4CBZ?format=jpg&name=large)

I think you know that most RAG systems still work like this: ask a question, grab some chunks, stuff them into a prompt, and pray

One shot. No second chances

Fine for easy stuff. Falls apart the second your question gets messy, the kind where you'd open five tabs and rethink your search terms twice

I dug into how the newer agentic RAG systems actually work under the hood, then built the whole thing as real, runnable code. An actual harness with a retrieval backend, a tool-using agent loop, and a token budget that forces itself to summarize before it blows up. Copy the whole thing

# The Problem In One Line

![Image](https://pbs.twimg.com/media/HNtAQv9XYAA0bRD?format=png&name=large)

Classic RAG finishes searching before it starts thinking. The model never gets a say in its own search. It just reacts to whatever got handed to it

Agentic RAG flips that. The model runs the search itself, in a loop, deciding when it has enough

**The 4 Piece Architecture:** **1\\ Loop** – model decides each round: search more or answer now **2\\ Search** – broad, multiple rewritten queries at once **3\\ Find + Open** – targeted digging inside specific documents **4\\ Summarize** – forced checkpoint before context blows up

Below is the full build. Two files. Runs locally against a sample corpus, swap the corpus for your real index and you're production ready

One honest note before you copy anything: treat every number here as a dial, not a rule

# File 1: the retrieval backend

This is the "dumb" part your agent controls

In production you'd swap this for Elasticsearch, a vector DB, whatever you already run. The interface matters. Every result gets a stable reference ID the moment it's first seen, and find/open only ever take that ID, never a raw file path

That's what keeps citations traceable across a long run

```python
"""
retrieval.py

search(queries)         -> broad recall, multiple queries merged + deduped
find(ref_id, query)     -> lexical search INSIDE one specific document
open(ref_id, start, n)  -> a bounded, line-numbered window of a document
"""

from __future__ import annotations
import re, glob, os
from dataclasses import dataclass, field
from collections import defaultdict

CORPUS_DIR = os.path.join(os.path.dirname(__file__), "corpus")
DEFAULT_WINDOW = 1800  # lines

def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())

@dataclass
class ReferenceRegistry:
    """Maps stable reference IDs <-> document paths, created once per run."""
    _by_id: dict[str, str] = field(default_factory=dict)
    _by_path: dict[str, str] = field(default_factory=dict)
    _counter: int = 0

    def get_or_create(self, path: str) -> str:
        if path in self._by_path:
            return self._by_path[path]
        self._counter += 1
        ref_id = f"R{self._counter}"
        self._by_id[ref_id] = path
        self._by_path[path] = ref_id
        return ref_id

    def resolve(self, ref_id: str) -> str:
        if ref_id not in self._by_id:
            raise KeyError(f"Unknown reference id: {ref_id}")
        return self._by_id[ref_id]

class RetrievalBackend:
    def __init__(self, corpus_dir: str = CORPUS_DIR):
        self.corpus_dir = corpus_dir
        self.registry = ReferenceRegistry()
        self._docs: dict[str, list[str]] = {}
        self._load_corpus()

    def _load_corpus(self) -> None:
        for path in glob.glob(os.path.join(self.corpus_dir, "*.txt")):
            with open(path, "r", encoding="utf-8") as f:
                self._docs[path] = f.read().splitlines()

    def search(self, queries: list[str], top_k_per_query: int = 10) -> list[dict]:
        if len(queries) > 5:
            raise ValueError("search() takes at most 5 query variants per call")

        best_score: dict[str, float] = defaultdict(float)
        best_snippet: dict[str, str] = {}

        for query in queries:
            q_tokens = set(_tokenize(query))
            if not q_tokens:
                continue
            for path, lines in self._docs.items():
                doc_tokens = _tokenize("\n".join(lines))
                overlap = sum(1 for t in doc_tokens if t in q_tokens)
                score = overlap / (len(doc_tokens) ** 0.5 + 1)
                if score > best_score[path]:
                    best_score[path] = score
                    best_snippet[path] = self._best_snippet(lines, q_tokens)

        ranked = sorted(best_score.items(), key=lambda kv: kv[1], reverse=True)
        results = []
        for path, score in ranked[:top_k_per_query]:
            if score <= 0:
                continue
            ref_id = self.registry.get_or_create(path)
            results.append({
                "reference_id": ref_id,
                "title": os.path.basename(path),
                "snippet": best_snippet[path],
                "score": round(score, 4),
            })
        return results

    def _best_snippet(self, lines: list[str], q_tokens: set[str], width: int = 1) -> str:
        best_line, best_hits = 0, -1
        for i, line in enumerate(lines):
            hits = sum(1 for t in _tokenize(line) if t in q_tokens)
            if hits > best_hits:
                best_hits, best_line = hits, i
        start = max(0, best_line - width)
        end = min(len(lines), best_line + width + 1)
        return " / ".join(lines[start:end]).strip()

    def find(self, reference_id: str, query: str, case_sensitive: bool = False) -> list[dict]:
        path = self.registry.resolve(reference_id)
        lines = self._docs[path]
        flags = 0 if case_sensitive else re.IGNORECASE
        hits = []
        for i, line in enumerate(lines):
            if re.search(re.escape(query), line, flags):
                hits.append({"line": i, "text": line.strip()})
        return hits

    def open(self, reference_id: str, start_line: int = 0, window: int = DEFAULT_WINDOW) -> dict:
        path = self.registry.resolve(reference_id)
        lines = self._docs[path]
        end_line = min(len(lines), start_line + window)
        numbered = [f"{i+1}\t{lines[i]}" for i in range(start_line, end_line)]
        return {
            "reference_id": reference_id,
            "title": os.path.basename(path),
            "start_line": start_line,
            "end_line": end_line,
            "total_lines": len(lines),
            "content": "\n".join(numbered),
        }
```

I tested this before writing a single line of the agent on top of it. Ran it against a sample revenue doc and an unrelated OCR runbook. Search correctly ranked the revenue doc first with a score of 1.87 versus 0.06 for the unrelated doc. find pulled every line mentioning "annual" with exact line numbers. open returned a clean numbered window. If your retrieval layer can't do this much on its own, fix that before you touch the agent loop

## File 2: the agent harness

This is the part that actually decides when to search, what to open, and when it has enough. It runs on Claude's tool use, tracks its own token spend, and forces itself to checkpoint before it blows the context window

```python
"""
agent.py

Run:
    export ANTHROPIC_API_KEY=sk-...
    python agent.py "What portion of iOS App revenue last quarter came from annual contracts?"

Requires: pip install anthropic
"""

from __future__ import annotations
import sys, os, json
import anthropic
from retrieval import RetrievalBackend

MODEL = "claude-sonnet-4-6"
MAX_CYCLES = 15
TOKEN_BUDGET = 128_000
WARN_AT_RATIO = 0.90

SYSTEM_PROMPT = """You are a research agent with access to search tools over an internal document corpus.

Rules you must follow:
1. You have a maximum of 15 reasoning cycles. Use them deliberately.
2. After every tool result, decide explicitly: do I have enough evidence to
   answer confidently, or do I need to keep digging?
3. If you need to keep digging, do not repeat a previous search query with
   only minor wording changes. Change the actual angle.
4. Use \`search\` for broad recall (up to 5 query variants at once).
   Use \`find\` to locate exact terms inside ONE document you already have a
   reference_id for. Use \`open\` to read a line-numbered window of a document.
5. Every factual claim in your final answer MUST cite a reference_id.
6. If you cannot find a confident answer within your cycle budget, say so
   explicitly instead of guessing.
"""

TOOLS = [
    {
        "name": "search",
        "description": "Broad search across the document corpus. Pass up to 5 rewritten query variants covering different angles of the same question.",
        "input_schema": {
            "type": "object",
            "properties": {
                "queries": {"type": "array", "items": {"type": "string"}, "maxItems": 5}
            },
            "required": ["queries"],
        },
    },
    {
        "name": "find",
        "description": "Targeted lexical search INSIDE one specific document, using a reference_id from search.",
        "input_schema": {
            "type": "object",
            "properties": {
                "reference_id": {"type": "string"},
                "query": {"type": "string"},
            },
            "required": ["reference_id", "query"],
        },
    },
    {
        "name": "open",
        "description": "Read a bounded, line-numbered window of a specific document (default 1800 lines).",
        "input_schema": {
            "type": "object",
            "properties": {
                "reference_id": {"type": "string"},
                "start_line": {"type": "integer", "default": 0},
            },
            "required": ["reference_id"],
        },
    },
]

class AgenticRAG:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.backend = RetrievalBackend()
        self.total_tokens = 0

    def _run_tool(self, name: str, tool_input: dict) -> dict:
        try:
            if name == "search":
                return {"results": self.backend.search(tool_input["queries"])}
            if name == "find":
                return {"hits": self.backend.find(tool_input["reference_id"], tool_input["query"])}
            if name == "open":
                return self.backend.open(tool_input["reference_id"], tool_input.get("start_line", 0))
            return {"error": f"unknown tool {name}"}
        except Exception as e:
            return {"error": str(e)}

    def _force_summary(self, messages: list[dict]) -> list[dict]:
        summary_request = messages + [{
            "role": "user",
            "content": (
                "You're approaching the token budget. Summarize your reasoning "
                "so far in under 300 words, and explicitly list every "
                "reference_id you still need. Do not answer yet."
            ),
        }]
        resp = self.client.messages.create(
            model=MODEL, max_tokens=500, system=SYSTEM_PROMPT, messages=summary_request,
        )
        summary_text = "".join(b.text for b in resp.content if b.type == "text")
        return [
            {"role": "user", "content": messages[0]["content"]},
            {"role": "assistant", "content": f"[Progress so far, summarized to save context]\n{summary_text}"},
        ]

    def run(self, question: str) -> str:
        messages = [{"role": "user", "content": question}]

        for cycle in range(1, MAX_CYCLES + 1):
            response = self.client.messages.create(
                model=MODEL, max_tokens=2000, system=SYSTEM_PROMPT, tools=TOOLS, messages=messages,
            )

            self.total_tokens += response.usage.input_tokens + response.usage.output_tokens
            usage_ratio = self.total_tokens / TOKEN_BUDGET
            print(f"[cycle {cycle}] stop_reason={response.stop_reason} tokens_used={self.total_tokens} ({usage_ratio:.0%} of budget)")

            if usage_ratio >= WARN_AT_RATIO:
                print("[budget] over 90% of token budget, forcing a summary checkpoint")
                messages = self._force_summary(messages)
                continue

            if response.stop_reason != "tool_use":
                return "".join(b.text for b in response.content if b.type == "text")

            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = self._run_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result),
                    })
            messages.append({"role": "user", "content": tool_results})

        return "Ran out of reasoning cycles without a confident answer. Try narrowing the question."

if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY first: export ANTHROPIC_API_KEY=sk-...")
        sys.exit(1)

    question = " ".join(sys.argv[1:]) or "What portion of iOS App revenue last quarter came from annual contracts?"
    agent = AgenticRAG()
    answer = agent.run(question)
    print("\n=== ANSWER ===")
    print(answer)
```

# How to actually run this

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-your-key-here

mkdir corpus
# drop your .txt documents into corpus/, or start with a couple test files

python agent.py "your question here"
```

You'll see live cycle-by-cycle output showing token spend and which tool the model reached for. That visibility alone is worth building this even if you never ship it, watching an agent choose search versus find versus open on a real question teaches you more about your own document structure than any dashboard will

# The 6 box checklist for adapting this to your own stack

```plaintext
☐ 1. Swap RetrievalBackend for your real search index. Keep the interface identical.
☐ 2. Keep the ReferenceRegistry pattern. Every doc gets one stable ID, always.
☐ 3. Never let search and find collapse into one tool. They solve different problems.
☐ 4. Track token usage exactly like this, warn at 90%, force a summary at the limit.
☐ 5. Make citations mandatory in the system prompt, not optional.
☐ 6. Cap cycles. 15 is a reasonable starting point, tune it against your own cost data.
```

## The one test that exposes a fake "agentic RAG"

Ask it: "Give me the exact reference\_id and location for that last claim."

Can't produce one? It's not doing agentic retrieval, it's just pattern matching on whatever got stuffed in the prompt.

> **Before you build any of this, run the gut check**

Only worth the extra complexity if all of these are true:

```plaintext
✅ Your questions are genuinely multi-step or buried across documents
✅ You're under a few hundred queries a day (token cost adds up fast)
✅ A wrong answer actually costs you something
```

**If you're running a simple FAQ bot for "what are your business hours," skip all of this. You'd be burning tokens on a Ferrari to buy milk..**

# The Real Takeaway

It's a systems decision: split the model's job (deciding what to search and when to stop) from the search stack's job (actually running the query). Once separated, you can upgrade either one on its own, swap the backend, tune the cycle cap, change the summarization trigger, without touching the other half.

Open question worth sitting with: how much of the gain here is the model being smart, versus just giving it more time, more tool calls, and a better policy for using them?

Worth testing before you assume you need the biggest model on the market

Save this so you don't lose it

Follow [@beamnxw](https://x.com/@beamnxw) for more technical posts :)

[my telegram channel](https://t.me/beamnxw11)

<video preload="none" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/amplify_video_thumb/2079331358074101760/img/QEbqk7t-HzsmgjqG.jpg" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"><source type="video/mp4" src="blob:https://x.com/d572875f-4de5-4368-8084-b37d1ebb36a0"></video>

![](https://pbs.twimg.com/amplify_video_thumb/2079331358074101760/img/QEbqk7t-HzsmgjqG.jpg?name=large)