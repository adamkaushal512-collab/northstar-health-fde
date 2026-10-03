# NorthStar Health — Data / RAG / Agent Build

## Phase 10

Phase 10 extends the Phase 9 executable prototype with a bounded retrieval-and-agent layer for MRI/CT prior authorization evidence investigation.

The objective is not to create an autonomous medical agent. The objective is to build a controlled investigation workflow that gathers case context through approved tools, retrieves candidate evidence, produces source-grounded summaries, and preserves the human decision boundary.

## Architecture Added

```text
Investigation Request
        ↓
Bounded Investigation Agent
        ├── authorization.get_case
        ├── payer.get_requirements
        └── clinical.get_records
        ↓
Hybrid-Ready Retrieval Layer
        ↓
Ranked Evidence + Provenance
        ↓
Grounded Evidence Synthesizer
        ↓
Grounding Guardrails
        ↓
Structured Investigation Result
        ↓
Human Review
```

## Bounded Agent

The agent has an explicit allow-listed sequence of tools. It cannot dynamically invent operations or directly access arbitrary enterprise systems.

Each tool execution produces a trace containing the tool name, status, and non-sensitive operational detail.

This makes orchestration observable and testable.

## Retrieval

Phase 9 used exact evidence-type matching.

Phase 10 introduces scored retrieval using:

- structured evidence-type matching
- lexical overlap
- deterministic ranking
- a minimum retrieval threshold

This creates the interface needed for later semantic/vector retrieval without weakening patient/case scoping or provenance.

## RAG Contract

The RAG contract is:

1. retrieve evidence
2. retain provenance
3. synthesize only from retrieved evidence
4. attach source references
5. validate grounding
6. return no summary when no grounded evidence exists

The current synthesizer is deterministic by design.

A production LLM can later replace the synthesizer behind the same interface, but it must satisfy the same grounding contract and evaluation suite.

## Why the LLM Boundary Is Still Replaceable

The system now has an `app/ai` boundary, but Phase 10 does not require an external API key.

This is intentional:

- the repository remains runnable for recruiters
- tests remain deterministic
- no PHI is sent externally
- retrieval and orchestration defects remain separable from model defects
- future model providers can be evaluated behind one stable interface

The AI layer is therefore production-shaped without coupling the project to one vendor prematurely.

## Grounding Controls

A requirement summary is valid only when it is backed by evidence IDs that correspond to provenance-valid retrieved evidence.

A requirement with no supporting evidence receives no generated summary.

Missing evidence remains distinct from source unavailability.

## Safety Boundary

The agent cannot:

- diagnose
- recommend treatment
- determine medical necessity
- approve or deny authorization
- modify source systems
- submit an authorization
- create unsupported evidence
- bypass human review

## Phase 10 Outcome

NorthStar Health now has a bounded agentic investigation workflow, ranked retrieval, provenance-aware RAG contracts, grounded evidence synthesis, tool traces, and grounding tests.

The next phase is **Phase 11 — AI Evaluation**, where the project will measure evidence retrieval quality, groundedness, missing-evidence behavior, failure handling, and workflow safety using a larger synthetic evaluation set.
