# Portfolio Walkthrough — From Customer Problem to Enterprise Scale

This document compresses 24 implementation phases into the story an FDE interviewer cares about.

## 1. Discover the real problem — Phases 1–6

The project begins with customer discovery rather than a model choice. The selected problem is MRI/CT prior-authorization exception investigation: specialists reconstruct payer requirements and clinical evidence across fragmented systems.

Outputs include workflow mapping, system/data discovery, use-case prioritization, and success metrics. The key product decision is to optimize **investigation quality and specialist effort**, not autonomous authorization.

## 2. Design the enterprise boundary — Phases 7–8

The architecture preserves source systems, introduces adapters, establishes provenance and human-review boundaries, and documents security/privacy/governance expectations.

The central safety principle is that AI may organize and summarize evidence but may not become the source of truth or decision maker.

## 3. Build the vertical slice — Phases 9–10

The FastAPI prototype evolves into a bounded investigation pipeline:

`case → payer requirements → clinical records → retrieval → grounded synthesis → validation → investigation result`.

The agent is deliberately constrained to allow-listed tools. Evidence is patient-scoped and requirement-specific.

## 4. Prove quality and safety — Phases 11–13

A version-controlled evaluation harness measures requirement accuracy, provenance, grounding, preservation of human review, and tool sequence.

Red-team tests cover prompt injection, cross-patient leakage, irrelevant evidence, missing provenance, and unsafe actions.

Deterministic fallback converts source outages, missing evidence, provenance failures, and system errors into explicit human/manual dispositions.

## 5. Productionize — Phases 14–16

The service gains configuration, resilience/error primitives, request context, health/readiness concepts, structured logging/metrics/tracing, CI, Docker packaging, Compose, and environment boundaries.

The portfolio deliberately stops short of claiming external infrastructure that is not actually deployed.

## 6. Pilot, release, and operate — Phases 17–20

Synthetic UAT scenarios establish acceptance criteria. Production readiness is an explicit go/no-go gate. Rollout is progressive, with safety regression triggering rollback and operational degradation pausing expansion.

Incident response distinguishes safety failures, service failures, and dependency degradation. The manual prior-auth process remains the safe fallback.

## 7. Learn, measure, and scale — Phases 21–24

Field feedback routes to red-team, evaluation, product, or engineering backlogs. Business-impact code models before/after metrics while clearly labeling them synthetic.

New use cases are disabled until they earn their own workflow, evaluation, red-team, guardrail, and UAT evidence. Enterprise-scale contracts add tenant isolation, capacity planning, and governance gaps.

## What this demonstrates as an FDE

- translating an ambiguous operational problem into a bounded technical use case;
- integrating around existing systems instead of replacing them;
- designing AI around evidence, provenance, evaluation, and human control;
- handling failure paths and operational reality, not just the happy path;
- connecting prototype work to deployment, adoption, impact, and scale; and
- communicating what is implemented versus what still requires a real customer environment.
