---
title: "State Machines: From Loops to Graphs (Explained)"
source: https://x.com/TheVixhal/status/2079274210367775052
author:
  - "[[@TheVixhal]]"
published: 2026-07-20
created: 2026-07-21
description: Every few months the agent-building world adopts a new abstraction, moving from chains to loops and now to graphs, and each of these turns o...
tags:
  - "clippings"
  - "agentic-engineering"
  - "state-machines"
---
![Image](https://pbs.twimg.com/media/HNsKZvWbMAAF2pS?format=jpg&name=large)

Every few months the agent-building world adopts a new abstraction, moving from chains to loops and now to graphs, and each of these turns out to be the same underlying idea with a different name.

That idea is the finite state machine, a formalism that has existed in textbooks since the 1950s, that specifies TCP and the control unit of your CPU, and that already exists in most codebases in an accidental form built out of Boolean flags and scattered conditionals.

Since implementing one deliberately costs almost nothing extra and comes with strong guarantees, it is worth understanding the pattern properly, so this article covers the theory, the implementation, and the reason agent frameworks are converging on it without acknowledging it.

# The core

A state machine answers a single question, which is that given the current state, when an event occurs, what is the next state? Written as a function, it looks like this:

```typescript
transition(state, event) -> nextState
```

Every program already behaves this way, because a React component, a request handler, a game loop, and an LLM agent all hold some state, receive some event, and move to a new state as a result.

Since this structure is present in every program whether or not anyone planned it, the only real decision a developer makes is where the transition logic lives, and usually it ends up scattered across event handlers and conditionals where nobody can see the complete picture.

Writing it as one explicit function gathers the complete behavior of the system into one place, and every benefit described in the rest of this article follows from that single move.

# The formal definition

A finite state machine is formally a 5-tuple:

M = (S, Σ, δ, s₀, F)

where:

- S is a finite set of states
- Σ is a finite set of events, called the input alphabet
- δ : S × Σ → S is the transition function
- s₀ ∈ S is the initial state
- F ⊆ S is the set of final states

Because S is finite and δ can be written down as a table, the complete behavior of the system can be enumerated, meaning every reachable state and every possible sequence of transitions can be listed and inspected.

Arbitrary code lacks this property because its state space is unbounded and its control flow depends on runtime values, and this difference is exactly why protocols, regex engines, and hardware get specified as state machines, since a finite specification can be checked exhaustively and, in safety-critical settings, proven correct.

One distinction from the theory appears often enough in practice to be worth knowing. If δ(state, event) yields exactly one next state, the machine is called a deterministic finite automaton (DFA), and if it can yield a set of possible next states, it is called a nondeterministic finite automaton (NFA).

Nondeterminism sounds abstract, but a regex engine compiles every pattern into an NFA and then either simulates it directly or converts it into a DFA through subset construction, which means that writing an expression like a+b\*c amounts to programming a state machine and letting a compiler construct it for you.

Every framework discussed later in this article, including the agent orchestration libraries, is a wrapper around this δ function, and keeping that in mind makes new tooling much easier to evaluate.

# The problem it solves: impossible states

Consider how data fetching usually gets modeled:

```typescript
let isLoading = false;
let isError = false;
let isSuccess = false;
let data = null;
let error = null;
```

Three booleans produce 2³ = 8 combinations, of which perhaps three are meaningful, and a combination like isLoading && isError describes no coherent situation at all, yet the type system permits it and eventually a race condition will construct it, producing a spinner rendered on top of an error message on top of stale data.

The problem grows exponentially because each additional flag doubles the state space while the number of valid states grows much more slowly, so a component with five flags has 32 possible combinations and maybe five legitimate ones.

The usual response is to write defensive conditions like if (isLoading && !isError && ...) that try to fence off the valid region by hand, and in a growing codebase some case always gets missed.

Modeling the same feature as a state machine begins with replacing the flags with an enumeration:

```typescript
type State = 'idle' | 'loading' | 'success' | 'failure';
```

Under this representation the combination of loading and error cannot even be written down, so the entire category of contradictory-flag bugs disappears at the type level rather than being caught in tests.

Functional programmers describe this as making illegal states unrepresentable, and a state machine applies the same principle to how a system evolves over time rather than to a single data structure.

Two guarantees follow immediately from the structure:

1. The system is always in exactly one state.
2. Movement is only possible along transitions you defined.

The practical weight of the second guarantee is easy to underestimate. In flag-based code any handler can fire at any moment and mutate anything, while in a state machine an event that has no transition defined from the current state simply does nothing.

When a user double-clicks a submit button, the second SUBMIT event arrives while the machine is in loading, and since loading defines no SUBMIT transition, the machine ignores it, which means the duplicate-submission bug never existed and no debounce, lock, or disabled-button flag was ever needed to prevent it.

# Implementation

The transition function is data, and the cleanest implementations treat it that way, which in most languages means a plain lookup table:

```typescript
const machine = {
  initial: 'idle',
  states: {
    idle: {
      FETCH: 'loading',
    },
    loading: {
      RESOLVE: 'success',
      REJECT: 'failure',
      CANCEL: 'idle',
    },
    success: {
      REFETCH: 'loading',
    },
    failure: {
      RETRY: 'loading',
    },
  },
};

function transition(state, event) {
  return machine.states[state]?.[event] ?? state; // undefined event: stay put
}
```

That one function is a complete state machine interpreter, and the tabular shape carries several practical consequences.

The full behavior of a feature fits on one screen, a diff of this object in code review shows behavior changes directly rather than requiring the reviewer to simulate control flow, and the object can be serialized, stored in a database, sent over the network, or rendered into a diagram automatically.

Testing also changes character, because states multiplied by events forms a finite table, so a test suite can walk the entire table instead of sampling paths through the code and hoping the important ones were covered.

The same machine can also be written as a switch statement:

```typescript
function transition(state: State, event: Event): State {
  switch (state) {
    case 'idle':
      return event.type === 'FETCH' ? 'loading' : state;
    case 'loading':
      switch (event.type) {
        case 'RESOLVE': return 'success';
        case 'REJECT': return 'failure';
        case 'CANCEL': return 'idle';
        default: return state;
      }
    case 'success':
      return event.type === 'REFETCH' ? 'loading' : state;
    case 'failure':
      return event.type === 'RETRY' ? 'loading' : state;
  }
}
```

This version is more verbose, but in TypeScript or Rust the compiler enforces exhaustiveness, so adding a new state and forgetting to handle it fails the build instead of failing in production.

Rust takes the idea furthest through the typestate pattern, in which each state becomes a distinct type and an invalid transition fails to compile at all.

Anyone who has written a Redux reducer or used useReducer has already written a function of the form (state, action) => nextState, so this pattern is more familiar than it might sound.

The difference is that most reducers allow any action to modify anything from any state, which quietly reintroduces the boolean-flag problem with better syntax, whereas a reducer becomes a genuine state machine once it checks the current state before considering the event, and that single change in ordering is what carries all of the guarantees described above.

# Finite state vs. context

A reasonable objection at this point is that real application state includes form inputs, arrays, and timestamps, none of which can be enumerated, so the finiteness requirement appears to rule out real programs.

The standard answer is to split state into two parts that play different roles. The finite state captures the mode the system is in, using values like idle, loading, editing, or disconnected, and this part stays qualitative, small, and enumerable.

The context, also called extended state, holds everything quantitative, such as form values, retry counts, and fetched data, and this part is allowed to be unbounded because the machine never enumerates it.

The machine governs the mode while the context travels alongside it, and a machine extended this way is formally called an extended state machine, with a transition function that returns more information:

```typescript
transition(state, context, event) -> (nextState, nextContext, actions)
```

The following example implements retries with a cap of three attempts:

```typescript
function transition(state, ctx, event) {
  if (state === 'failure' && event.type === 'RETRY') {
    if (ctx.retries < 3) {
      return ['loading', { ...ctx, retries: ctx.retries + 1 }, ['fetch']];
    }
    return ['gaveUp', ctx, ['notifyUser']];
  }
  // ...
}
```

Three standard concepts appear in this code and deserve names. A guard is a condition attached to a transition, and the check ctx.retries < 3 is one, allowing the same RETRY event to lead to loading while attempts remain and to gaveUp once they run out.

An action is a side effect that a transition triggers, and the returned \['fetch'\] is one, with the important detail being that the machine only decides which effects should occur and returns them, while an interpreter outside the function actually executes them, which keeps the transition function pure and makes testing it possible without any mocks.

Redux middleware and Elm's pattern of returning commands from its update function follow the same separation. Entry and exit actions round out the set, and these are effects attached to entering or leaving a state rather than to any particular edge, so that entering loading starts a spinner and a timeout while exiting loading cancels both, regardless of which of the four possible edges was taken in or out.

Exit actions in particular eliminate the family of bugs around leaked timers, dangling subscriptions, and forgotten cleanup, because when the cancellation is attached to the exit of loading, every path out of that state runs it and no code path can leave the timer running.

Achieving the same reliability with flags requires remembering the cleanup in every handler that could leave loading mode, and in practice one handler always forgets.

# Mealy and Moore machines

The classical literature distinguishes two variants of the machine according to where outputs attach. In a Moore machine the output depends on the current state alone, as in a traffic light that stays lit for as long as the machine remains in the green state, so outputs effectively live on the nodes of the diagram.

In a Mealy machine the output depends on the state and the event together, as in a vending machine that dispenses when a COIN event arrives during the idle state, so outputs live on the edges instead.

The two variants are equivalent in expressive power and can be converted into each other, and real systems mix both, since entry and exit actions are Moore-flavored while transition actions are Mealy-flavored.

Beyond helping with older papers and hardware documentation, the distinction supplies a genuinely useful design question, namely whether a given effect should happen because the system is in a state or because of how it arrived there, and since the two answers behave differently under edge cases, conflating them produces subtle bugs.

# Where this already runs

Several major pieces of infrastructure are specified as state machines, and looking at them shows how far the pattern predates its current rediscovery.

TCP defines every connection through its state diagram, whose states include LISTEN, SYN\_SENT, ESTABLISHED, FIN\_WAIT\_1, and TIME\_WAIT. RFC 793 specified the protocol as a state diagram back in 1981 because prose was too ambiguous for something this critical, and to this day disagreements between implementations get settled by pointing at the machine.

Regex engines run on DFAs, which process each input character in constant time with no backtracking, and grep owes its speed directly to this property of the underlying model rather than to any implementation cleverness.

Game AI has used the pattern since the arcade era, with enemy behavior following transitions such as patrol to chase to search and back to patrol, driven by events like seeing or losing the player. The ghosts in Pac-Man are four small state machines, and their famously distinct personalities come entirely from four different transition tables.

In hardware the pattern is foundational, since a CPU is a clocked state machine and both Verilog and VHDL treat FSMs as a primary design idiom. Traffic lights, elevators, and vending machines became the textbook examples precisely because failures in those systems cause physical harm, so their logic had to be built on something checkable.

UI code contains the same structure implicitly, because every form passes through stages like pristine, editing, validating, submitting, and finally succeeded or failed, and dropdowns, media players, and drag interactions have the same character.

The familiar bug where a modal closes but its dark overlay remains on screen occurs when the system occupies a state combination its designers never intended, which is precisely the situation an explicit machine makes unrepresentable.

# Agents

An agent graph describes how an agent moves between steps as it plans, calls tools, evaluates results, retries, asks a human, and eventually finishes.

The field started with linear pipelines, moved to DAGs after admitting that agents fail and branch, and then had to allow cycles after admitting that agents also retry until verified and loop through rounds of human feedback, which leaves a directed cyclic graph with labeled edges, a start node, and terminal nodes.

Mapping those parts onto the 5-tuple, the nodes are S, the edge labels are Σ, the edges are δ, the start node is s₀, and the terminal nodes are F, so the agent graph reconstructs the finite state machine under a new name.

A realistic agent written explicitly as a machine looks like this:

```typescript
const agent = {
  initial: 'planning',
  states: {
    planning: {
      PLAN_READY: 'executing',
      NEEDS_INFO: 'awaitingHuman',
    },
    executing: {
      TOOL_RESULT: 'evaluating',
      TOOL_ERROR: 'executing',      // self-loop: retry the tool
      BUDGET_EXCEEDED: 'failed',
    },
    evaluating: {
      VERIFIED: 'done',
      NOT_GOOD_ENOUGH: 'planning',  // a cycle, which a DAG cannot express
      UNSAFE: 'awaitingHuman',
    },
    awaitingHuman: {
      APPROVED: 'executing',
      REJECTED: 'failed',
      CLARIFIED: 'planning',
    },
    done: {},    // final
    failed: {},  // final
  },
};
```

Making the machine explicit gives agents several properties that matter in production.

Retry logic becomes a guarded edge, since the behavior of retrying until verified reduces to the single transition from evaluating back to planning with a guard requiring attempts to stay under a maximum, so runaway loops are ruled out by the structure itself instead of by a counter that someone hopefully remembered to add to a while loop.

Control flow also stays out of the model's hands, which matters because LLM output is nondeterministic and letting it drive control flow directly produces agents that declare themselves finished when they are not.

Under the machine, model output first gets classified into an event such as VERIFIED or UNSAFE, and the machine then checks whether that event has a legal transition from the current state, so a model can hallucinate an event but a hallucinated event with no matching edge goes nowhere, and the safety-critical route from UNSAFE to awaitingHuman ends up enforced by a lookup table rather than by instructions in a system prompt.

Long-running agents become persistable as well, because the pair of current state and context is one small serializable value, so an agent waiting three days for human approval reduces to writing the pair ('awaitingHuman', ctx) into a database row, terminating the process, and rehydrating when the approval webhook fires.

Durable workflow engines such as Temporal and AWS Step Functions are built on exactly this idea, and Step Functions goes as far as requiring the machine to be written out as JSON.

Debugging gets simpler for the same reason, since the question of what the agent is doing becomes a single-column query and the question of how it got there becomes the event history, whereas answering the same questions about a free-form loop requires reconstructing behavior from traces.

Multi-agent systems pair the machine naturally with the actor model, in which each agent is an actor holding private state and communicating only through messages, while each actor's internal behavior is a state machine whose events are the incoming messages.

Erlang built this exact combination in the 1980s, its OTP framework ships a state-machine actor primitive called gen\_statem, and the result has run telecom switches at extreme uptime for decades, which means multi-agent architecture is also a rediscovery, though one that belongs to a separate article.

# Statecharts

Flat state machines fail to scale in one specific way, which shows up as soon as a system has independent concerns.

A text editor where bold, italic, and underline can each be toggled independently needs flat states like bold\_italic, bold\_underline, and bold\_italic\_underline to cover the combinations, so the combinatorial explosion from the boolean-flag section returns, now with strings instead of booleans.

David Harel addressed this in 1987 with statecharts, introduced in his paper "Statecharts: A Visual Formalism for Complex Systems," which remains genuinely readable today. The formalism adds three constructs to the plain machine:

- **Hierarchy** allows states to contain child states, so if connected contains syncing and idle, a single DISCONNECT transition defined on the parent covers every child and the duplication of shared transitions ends.
- **Parallel regions** let independent concerns run side by side within one machine, so bold, italic, and underline become three parallel two-state regions, giving 2 + 2 + 2 = 6 states instead of 2 × 2 × 2 = 8 combined ones, and the gap widens rapidly as more regions are added.
- **History states** make a parent remember which child was last active, so re-entering the parent resumes there, which is the mechanism behind a pause menu that returns exactly where you left off.

Statecharts remain state machines formally and carry the same guarantees, since these constructs only compress the description of large machines rather than changing the model, and the state diagrams in UML are statecharts by another name.

# When not to use this

Genuinely sequential logic that runs A then B then C with no waiting, no external events, and no failure branches worth modeling belongs in a plain function, because state machines earn their cost only when events and time enter the picture.

Truly continuous state, as in a physics simulation or a numerical solver, gains nothing from the framing either, because there are no discrete modes to model, and at the other end of the scale a two-state toggle needs nothing beyond useState(false).

A reliable trigger in practice is the moment a second boolean appears that interacts with the first, or the moment a comment appears that reads "but only if we're currently...", because at that point the code has already grown the shape of a machine and would benefit from becoming one explicitly.

# Wrapping up

Loops and graphs both turned out to be state machines once their states, events, and transitions were named, and whatever abstraction arrives after them can be judged the same way.

If it can answer those three questions, it is a state machine that can be reasoned about, and if it cannot, it is scattered control flow with better marketing.