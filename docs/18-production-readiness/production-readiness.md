# Phase 18 — Production Readiness

Production readiness is an explicit go/no-go gate.

Blocking checks include automated tests, AI evaluation, red-team safety, guardrails/human fallback, security/privacy review, deployment rollback capability, observability, runbooks, and ownership.

Any failed blocking control produces `no_go`. This prevents schedule pressure from silently overriding safety or reliability requirements.

For a real healthcare deployment, customer security review, HIPAA/BAA obligations, IAM, data retention, vendor/model terms, infrastructure validation, and disaster recovery evidence would also be required.
