#!/usr/bin/env python3
"""
LLM Wiki linter.

Reports findings against the conventions in CLAUDE.md § Workflows → Lint:
broken wikilinks, ambiguous wikilinks, orphan pages, index drift,
frontmatter drift, and frontmatter-page-type mismatches.

Read-only: makes no changes. Pipe stdout to LINT_REPORT.md if you want the
output as a file.

Usage: python3 bin/wiki_lint.py [vault_path]

If vault_path is omitted, the script assumes it lives at <vault>/bin/.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT_PAGES = ["CLAUDE.md", "index.md", "log.md", "Welcome.md"]
WIKI_DIRS = ["wiki/sources", "wiki/entities", "wiki/concepts", "wiki/syntheses"]

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans so wikilinks inside
    them are not parsed as links. Preserves line count by replacing with
    spaces of equal length, which keeps any future line-based reporting
    correct."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        # Fenced code block (``` or ~~~) at start of line
        if (i == 0 or text[i-1] == "\n") and (text.startswith("```", i) or text.startswith("~~~", i)):
            fence = text[i:i+3]
            j = text.find("\n" + fence, i + 3)
            if j == -1:
                # unclosed fence — treat rest as code
                out.append(re.sub(r"[^\n]", " ", text[i:]))
                i = n
                continue
            j_end = text.find("\n", j + 4)
            if j_end == -1:
                j_end = n
            else:
                j_end += 1
            out.append(re.sub(r"[^\n]", " ", text[i:j_end]))
            i = j_end
            continue
        # Inline code span (single backtick — keeps things simple)
        if text[i] == "`":
            j = text.find("`", i + 1)
            if j == -1:
                out.append(text[i])
                i += 1
                continue
            out.append(re.sub(r"[^\n]", " ", text[i:j+1]))
            i = j + 1
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, text[end + 5:]


def collect_links(text):
    cleaned = strip_code(text)
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(cleaned)]


def collect_files(vault: Path):
    files = []
    for r in ROOT_PAGES:
        p = vault / r
        if p.exists():
            files.append(p)
    for d in WIKI_DIRS:
        d_path = vault / d
        if d_path.exists():
            files.extend(sorted(d_path.glob("*.md")))
    return files


def main(argv):
    if len(argv) > 1:
        vault = Path(argv[1]).resolve()
    else:
        vault = Path(__file__).resolve().parent.parent

    files = collect_files(vault)
    if not files:
        print(f"No wiki files found under {vault}")
        sys.exit(1)

    rel = {f: f.relative_to(vault).as_posix() for f in files}

    by_relpath = {rel[f]: f for f in files}
    by_relpath_noext = {rel[f][:-3]: f for f in files}
    by_basename = defaultdict(list)
    for f in files:
        by_basename[f.stem].append(f)

    contents = {}
    fms = {}
    alias_to_file = {}
    for f in files:
        text = f.read_text()
        contents[f] = text
        fm, _ = parse_frontmatter(text)
        fms[f] = fm
        if "aliases" in fm:
            v = fm["aliases"]
            if v.startswith("[") and v.endswith("]"):
                inner = v[1:-1]
                for a in inner.split(","):
                    a = a.strip().strip("'").strip('"')
                    if a:
                        alias_to_file[a.lower()] = f

    def resolve(target):
        if target in by_relpath_noext:
            return by_relpath_noext[target]
        if target + ".md" in by_relpath:
            return by_relpath[target + ".md"]
        base = target.split("/")[-1]
        if base in by_basename:
            cands = by_basename[base]
            if len(cands) == 1:
                return cands[0]
            return ("ambiguous", cands)
        if target.lower() in alias_to_file:
            return alias_to_file[target.lower()]
        return None

    inbound = defaultdict(set)
    broken = []
    ambiguous = []

    for f in files:
        for raw in collect_links(contents[f]):
            r = resolve(raw)
            if r is None:
                broken.append((rel[f], raw))
            elif isinstance(r, tuple) and r[0] == "ambiguous":
                ambiguous.append((rel[f], raw, [rel[c] for c in r[1]]))
            elif r != f:
                inbound[r].add(f)

    orphans = []
    for f in files:
        if rel[f] in ROOT_PAGES:
            continue
        if not inbound[f]:
            orphans.append(rel[f])

    index_text = (vault / "index.md").read_text() if (vault / "index.md").exists() else ""
    index_targets = set()
    for link in collect_links(index_text):
        r = resolve(link)
        if isinstance(r, Path):
            index_targets.add(r)

    missing_from_index = []
    for f in files:
        if "wiki/" not in rel[f]:
            continue
        if f not in index_targets:
            missing_from_index.append(rel[f])

    fm_issues = []
    for f in files:
        if "wiki/" not in rel[f]:
            continue
        fm = fms[f]
        expected = None
        if "wiki/sources/" in rel[f]:
            expected = "source"
        elif "wiki/entities/" in rel[f]:
            expected = "entity"
        elif "wiki/concepts/" in rel[f]:
            expected = "concept"
        elif "wiki/syntheses/" in rel[f]:
            expected = "synthesis"
        actual = fm.get("type", "")
        if actual != expected:
            fm_issues.append((rel[f], f"type='{actual}' expected '{expected}'"))
        for required in ("title", "created", "updated"):
            if required not in fm:
                fm_issues.append((rel[f], f"missing required: {required}"))

    broken_counts = defaultdict(int)
    broken_sources = defaultdict(set)
    for src, tgt in broken:
        broken_counts[tgt] += 1
        broken_sources[tgt].add(src)

    print("=" * 72)
    print("LLM WIKI LINT REPORT")
    print("=" * 72)
    print(f"Vault: {vault}")
    print(f"Files audited: {len(files)} ({sum(1 for f in files if 'wiki/' in rel[f])} wiki pages)")
    print()

    print(f"--- BROKEN WIKILINKS ({len(broken)} total, {len(broken_counts)} unique) ---")
    if not broken:
        print("  (none)")
    else:
        for tgt in sorted(broken_counts, key=lambda t: -broken_counts[t]):
            print(f"  [[{tgt}]]  ({broken_counts[tgt]} refs)")
            for src in sorted(broken_sources[tgt]):
                print(f"      ↳ {src}")
    print()

    print(f"--- AMBIGUOUS WIKILINKS ({len(ambiguous)}) ---")
    if not ambiguous:
        print("  (none)")
    else:
        for src, tgt, cands in ambiguous:
            print(f"  {src}: [[{tgt}]] could be {cands}")
    print()

    print(f"--- ORPHAN PAGES ({len(orphans)}) ---")
    if not orphans:
        print("  (none)")
    else:
        for o in orphans:
            print(f"  {o}")
    print()

    print(f"--- INDEX DRIFT ({len(missing_from_index)}) ---")
    if not missing_from_index:
        print("  (none)")
    else:
        for m in missing_from_index:
            print(f"  {m}")
    print()

    print(f"--- FRONTMATTER ISSUES ({len(fm_issues)}) ---")
    if not fm_issues:
        print("  (none)")
    else:
        for path, issue in fm_issues:
            print(f"  {path}: {issue}")
    print()

    print("--- STATS ---")
    by_type = defaultdict(int)
    stub_count = 0
    for f in files:
        if "wiki/" not in rel[f]:
            continue
        by_type[fms[f].get("type", "unknown")] += 1
        tags = fms[f].get("tags", "")
        if "stub" in tags:
            stub_count += 1
    for t in ("source", "entity", "concept", "synthesis"):
        if t in by_type:
            print(f"  {t}: {by_type[t]}")
    print(f"  stubs: {stub_count}")

    # Exit non-zero if any real issues
    has_issues = bool(broken or ambiguous or orphans or missing_from_index or fm_issues)
    sys.exit(1 if has_issues else 0)


if __name__ == "__main__":
    main(sys.argv)
