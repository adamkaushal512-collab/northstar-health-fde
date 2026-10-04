# NorthStar Incident Runbook

## Safety regression
1. Stop or roll back the affected rollout.
2. Preserve audit/correlation references.
3. Route work to the established human/manual workflow.
4. Reproduce the failure in evaluation/red-team tests.
5. Do not resume rollout until the blocking regression is resolved.

## Service unavailable
1. Confirm liveness/readiness and recent deployment state.
2. Restore the last known-good service version.
3. Keep authorization operations on the manual fallback path.
4. Capture timeline, impact, and corrective actions.

## Dependency degraded
1. Identify the unavailable source.
2. Do not convert unavailability into `evidence_not_found`.
3. Use Phase 13 fallback/handoff.
4. Restore connectivity and reconcile affected cases.
