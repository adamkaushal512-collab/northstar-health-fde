# NorthStar Health — Red Team / Safety Testing

## Phase 12

Phase 12 converts known adversarial risks into reproducible safety tests for the MRI/CT prior-authorization investigation workflow.

The synthetic red-team suite covers prompt injection in retrieved content, cross-patient evidence leakage, irrelevant evidence, missing provenance, and unsafe state-changing action requests.

Retrieved clinical content is treated as untrusted data rather than instructions. Patient scope must be established before retrieval. Evidence without trustworthy provenance cannot become verified support. The agent remains read-oriented; approval, denial, record modification, and other state-changing operations remain outside its allow-list.

The controlled baseline requires a 100% block rate for these known attacks. This is a regression gate, not a claim that the system is universally secure or immune to novel prompt injection.

For an FDE, every discovered unsafe behavior should become a reproducible case: reproduce it, add a test, implement a control, add regression coverage, and document residual risk.

Phase 13 will build explicit runtime guardrails, degraded modes, escalation, and human fallback on top of these safety requirements.
