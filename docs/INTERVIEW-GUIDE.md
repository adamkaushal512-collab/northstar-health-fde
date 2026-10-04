# Interview Guide

## 30-second version

> NorthStar Health is an FDE portfolio project for MRI/CT prior-authorization evidence investigation. It connects authorization, payer, and clinical-record boundaries through adapters, uses a bounded agent and retrieval pipeline to map clinical evidence to payer requirements, preserves provenance, and routes uncertainty or outages to human/manual workflows. I then took it through AI evaluation, red-team testing, production engineering, CI/observability, deployment, rollout, incident response, business-impact measurement, and enterprise-scale design. The public implementation uses synthetic data and never lets AI make the authorization decision.

## Two-minute version

Start with the operational problem, not the model.

A specialist needs to reconstruct a prior-auth case across fragmented systems. The first design decision was therefore to preserve systems of record and put adapters around them rather than create a new source of truth. A bounded investigation agent gathers the case, payer requirements, and patient-scoped clinical records. Retrieval ranks evidence against each requirement; grounded synthesis summarizes only retrieved evidence; provenance and grounding validators catch unsafe output.

The key safety distinction is between **evidence not found** and **source unavailable**. If the clinical source is down, NorthStar does not infer that evidence is absent. Deterministic fallback routes source failures to manual operations, missing evidence to specialist review, and provenance failures to safety review. Human review remains mandatory.

I treated AI quality as an engineering problem: version-controlled evaluation cases measure requirement accuracy, provenance, grounding, human-review preservation, and tool sequence. A separate red-team harness covers prompt injection, cross-patient leakage, irrelevant evidence, missing provenance, and unsafe actions.

Finally, I productionized the vertical slice with CI, Docker, environment boundaries, resilience, observability primitives, UAT/readiness gates, progressive rollout, incident response, feedback, impact measurement, and enterprise governance contracts.

## Strong technical talking points

### Why adapters?
They isolate system-specific contracts and failures from domain logic. Synthetic adapters can later be replaced with real FHIR/EHR/payer integrations without rewriting the investigation service.

### Why a bounded agent?
Prior authorization is operationally sensitive. An allow-listed sequence is easier to reason about, evaluate, audit, and secure than an open-ended autonomous agent.

### Why provenance?
A summary without a traceable source is not operational evidence. Provenance is part of the data contract, not decorative metadata.

### Why modular monolith?
For one vertical slice, microservices would add deployment and debugging overhead before independent scaling/ownership justified it. Package boundaries preserve future extraction seams.

### Why synthetic data?
It makes the portfolio safe and reproducible. The tradeoff is that real integration behavior, clinical validity, adoption, and ROI are intentionally unproven.

## Questions you should expect

### “Where is the actual LLM?”
The portfolio focuses on the **grounding and control contract** rather than depending on a proprietary model API. `GroundedEvidenceSynthesizer` represents the constrained synthesis boundary. In a customer deployment, a model provider could be inserted behind that interface only after privacy/security terms, evaluation, latency/cost, and data-handling requirements were validated.

### “Is this really RAG?”
It implements the core retrieval-and-grounding pattern over synthetic clinical records and payer requirements, with ranking, provenance, and grounded summaries. It is intentionally small-scale and deterministic for reproducibility; a production corpus could replace the retrieval implementation with hybrid/vector infrastructure while preserving the same evidence contract.

### “Why not let the model decide whether to approve?”
That is outside the chosen trust boundary. The system accelerates evidence investigation and exposes uncertainty; the human specialist retains the operational decision.

### “What happens if the EHR is down?”
The source becomes `source_unavailable`, not `evidence_not_found`. The fallback layer routes the case to the manual workflow and preserves the reason code for audit/operations.

### “How would you connect a real EHR?”
Implement the adapter contract using the customer's supported FHIR/API/event interfaces, identity/auth model, rate limits, and data semantics; validate mappings and freshness; then run integration, evaluation, security, and UAT gates before rollout.

### “What would you improve next?”
Use real customer workflow telemetry to calibrate retrieval/evaluation; add a production model gateway; persist audit events; connect OpenTelemetry/exporters; add contract/integration/load tests; integrate IAM and secrets management; and validate the workflow with real specialists under customer governance.

## What not to claim

Do not say:

- “This is HIPAA compliant.”
- “This has been deployed in a hospital.”
- “The model is clinically validated.”
- “It reduced prior-auth time by X% in production.”
- “The AI determines medical necessity.”

Instead say that the repository demonstrates the engineering patterns and identifies the controls a real deployment would need.
