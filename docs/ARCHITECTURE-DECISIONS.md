# Architecture Decisions and Tradeoffs

## ADR-1 — Preserve enterprise systems of record

**Decision:** NorthStar assembles investigation context but does not become the authoritative store for authorization, payer, or clinical facts.

**Why:** Enterprise healthcare data already has ownership, access, retention, and correction semantics. Duplicating authority would increase governance risk.

**Tradeoff:** Runtime behavior depends on upstream availability, so the design needs explicit source-status and fallback semantics.

## ADR-2 — Adapter boundaries around external systems

**Decision:** Source-specific access is isolated in `app/adapters/`.

**Why:** Keeps domain logic stable when a customer has different EHR, payer, authorization, authentication, or transport details.

**Tradeoff:** Adapters add interfaces and mapping work, but reduce coupling and make failures easier to classify.

## ADR-3 — Bounded orchestration over open-ended autonomy

**Decision:** The investigation agent follows an explicit, allow-listed sequence.

**Why:** Predictability, auditability, testability, and least privilege are more important than unconstrained agent flexibility for this workflow.

**Tradeoff:** Less autonomous exploration; new tools/workflows require deliberate engineering and validation.

## ADR-4 — Evidence/provenance is the primary AI contract

**Decision:** Evidence items include source system, source record, date, requirement mapping, retrieval score, and provenance validity.

**Why:** Specialists need to verify why a claim is present. Fluent unsupported text is not useful operationally.

**Tradeoff:** Stronger contracts reduce flexibility and require upstream metadata quality.

## ADR-5 — Separate missing evidence from unavailable evidence

**Decision:** Requirement status supports `evidence_found`, `evidence_not_found`, and `source_unavailable`.

**Why:** Treating an outage as absence could create a materially misleading investigation.

**Tradeoff:** Downstream UI and operations must handle an additional state and retry/manual workflows.

## ADR-6 — Human review is invariant

**Decision:** The investigation result requires human review; fallback can increase scrutiny but never remove it.

**Why:** The selected use case is evidence investigation, not autonomous authorization or medical-necessity decision-making.

**Tradeoff:** The system optimizes specialist effort rather than maximizing automation rate.

## ADR-7 — Modular monolith for the vertical slice

**Decision:** Keep one deployable Python/FastAPI application with strong internal package boundaries.

**Why:** It minimizes operational complexity during discovery and pilot while preserving clean seams.

**Tradeoff:** Independent scaling/deployment is limited until components are extracted. Extraction should be driven by measured load, ownership, reliability, or release-cadence needs—not architecture fashion.

## ADR-8 — Deterministic portfolio implementation

**Decision:** Keep synthetic data and deterministic retrieval/synthesis behavior in the public portfolio.

**Why:** Reproducibility, safe publication, and easy evaluation are more valuable here than depending on a paid model API.

**Tradeoff:** The repository demonstrates the model boundary and safety/evaluation architecture, not production LLM quality. A real model must earn deployment through customer-specific evaluation and governance.

## ADR-9 — Separate AI evaluation from unit testing

**Decision:** Maintain version-controlled eval and red-team datasets in addition to pytest regression tests.

**Why:** A function can be technically correct while AI behavior is ungrounded or unsafe.

**Tradeoff:** Evaluation datasets become maintained product assets and need expansion as field failures appear.

## ADR-10 — Progressive rollout with manual fallback

**Decision:** Production rollout can continue, pause, or roll back based on safety and operational signals, with an established manual workflow always available.

**Why:** Deployment success does not prove workflow safety or usefulness.

**Tradeoff:** Maintaining a fallback path costs operational capacity, but materially reduces rollout risk.
