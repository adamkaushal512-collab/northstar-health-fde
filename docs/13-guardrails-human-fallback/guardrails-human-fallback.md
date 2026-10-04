# NorthStar Health — Guardrails + Human Fallback

## Phase 13
Phase 13 turns prior safety principles into executable runtime behavior.

The AI workflow remains an investigation aid: it cannot approve or deny authorization, determine medical necessity, or silently turn uncertainty into an operational decision.

### Runtime dispositions
- `continue_review`: evidence assembly completed; human decision remains required.
- `human_review`: incomplete or untrusted evidence requires specialist review.
- `manual_workflow`: dependency/source failures require the established manual path.

### Machine-readable fallback reasons
The runtime emits explicit reasons such as `source_unavailable`, `insufficient_evidence`, `provenance_failure`, and `system_error`.

### Escalation routing
Operational outages route to manual operations; provenance failures route to safety review; evidence gaps route to specialist review.

### Human handoff
The handoff preserves case ID, destination queue, reason codes, trusted evidence IDs, unavailable sources, and the audit reference. This prevents specialists from reconstructing the investigation from scratch.

### Fail-safe principle
`evidence_not_found` is different from `evidence_could_not_be_checked`. Source unavailability is never interpreted as proof that evidence does not exist.

### FDE value
Fallback is part of the primary product path. Enterprise AI must remain useful and safe when dependencies fail or evidence is incomplete.

Phase 14 will harden the service for production operation.
