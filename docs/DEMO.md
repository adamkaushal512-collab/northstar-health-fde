# NorthStar Health — 5-Minute Interview Demo

The goal is to demonstrate the **FDE story**, not every file in the repository.

## Before the interview

```bash
source .venv/bin/activate
python -m pytest -q
```

Optionally keep two terminals ready: one for the demo script and one for the API.

## 0:00–0:45 — Customer problem

Say:

> Prior-authorization specialists often have to reconstruct a case across authorization, payer, and clinical systems. The hard part is not generating prose; it is determining what the payer requires, locating trustworthy patient-scoped evidence, preserving provenance, distinguishing missing evidence from unavailable systems, and keeping the human specialist in control.

Point to the architecture diagram in the README.

## 0:45–1:30 — Architecture

Explain the path:

`systems of record → adapters → bounded agent → retrieval → grounded synthesis → validation/guardrails → specialist`.

Emphasize two design choices:

1. The agent has an explicit allow-listed tool sequence rather than open-ended autonomy.
2. Source unavailability is a first-class state; it is never silently converted into evidence absence.

## 1:30–2:45 — Run one investigation

```bash
python scripts/demo.py
```

Use `AUTH-1001` unless you specifically want another synthetic case:

```bash
python scripts/demo.py AUTH-1001
```

Show:

- payer requirements;
- `evidence_found` / `evidence_not_found` status;
- evidence source and source-record provenance;
- tool trace;
- fallback disposition;
- `human_review_required=True`;
- audit reference.

Say:

> The output is intentionally evidence-centric rather than a free-form recommendation. The system organizes the investigation; it does not make the authorization decision.

## 2:45–3:30 — Evaluation and red team

```bash
python -m app.evals.runner
python -m app.redteam.runner
```

Explain that conventional unit/API tests are not enough for an AI workflow. The repository separately evaluates requirement accuracy, provenance, grounding, preservation of human review, and bounded tool sequencing, then exercises adversarial cases such as prompt injection and cross-patient leakage.

## 3:30–4:15 — Failure path

Open:

- `app/runtime/safe_investigation.py`
- `app/guardrails/fallback.py`
- `docs/20-monitoring-incident-response/runbook.md`

Say:

> I designed the failure path before treating this as production-ready. Source outages route to the established manual workflow; insufficient evidence routes to specialist review; provenance failures route to safety review.

## 4:15–5:00 — Production/FDE lifecycle

Show:

- `.github/workflows/ci.yml`
- `Dockerfile`
- `deploy/`
- `app/observability/`
- `docs/PORTFOLIO-WALKTHROUGH.md`

Close with:

> The project goes from discovery through production operations and enterprise scale. The code is deliberately synthetic, so I can demonstrate the architecture and controls without pretending I have a hospital deployment or real PHI.

## Optional API demo

```bash
uvicorn app.main:app --reload
```

Then:

```bash
curl -X POST http://127.0.0.1:8000/investigations \
  -H 'Content-Type: application/json' \
  -d '{"authorization_case_id":"AUTH-1001"}'
```

## If asked to go deeper

Choose the branch that matches the interviewer:

- **AI/ML:** retrieval, grounding, evals, red team.
- **Backend:** FastAPI, schemas, adapters, resilience, testing.
- **Platform/SRE:** CI, Docker, observability, readiness, rollout, incidents.
- **Security:** patient scoping, provenance, prompt injection, human boundary, tenant isolation.
- **Product/FDE:** discovery, workflow mapping, success metrics, adoption, impact, expansion.
