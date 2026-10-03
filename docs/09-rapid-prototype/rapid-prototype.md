# NorthStar Health — Rapid Prototype

## Phase 9 — Rapid Prototype

Phase 9 converts the architecture into the first executable end-to-end vertical slice for **AI-assisted MRI/CT prior authorization evidence investigation**.

The prototype intentionally uses synthetic data and deterministic retrieval. It proves the workflow contracts, adapter boundaries, provenance, missing-data semantics, human-review boundary, and testability before a production LLM or live healthcare integration is introduced.

## Implemented Slice

The prototype provides:

- FastAPI investigation API
- typed Pydantic request/response contracts
- synthetic authorization, payer, and clinical adapters
- deterministic requirement-to-evidence retrieval
- source provenance
- explicit `evidence_not_found` behavior
- explicit `source_unavailable` behavior
- mandatory human review
- audit correlation reference
- automated workflow and API tests

## Flow

```text
POST /investigations
        ↓
Authorization Adapter
        ↓
Payer Requirements
        ↓
Clinical Records
        ↓
Evidence Retrieval
        ↓
Requirement ↔ Evidence Mapping
        ↓
Provenance Validation
        ↓
Structured Investigation Result
        ↓
Human Review
```

## Synthetic Case

`AUTH-1001` models a lumbar MRI authorization exception. The payer requires physical-therapy, medication-history, and clinical-exam evidence. The synthetic EHR contains physical-therapy and examination evidence but intentionally lacks medication-history evidence.

The expected result is therefore two `evidence_found` requirements and one `evidence_not_found` requirement. The latter means only that supporting evidence was not found in the searched source; it does not assert that treatment never occurred.

## Why No External LLM Yet

Phase 9 deliberately keeps the evidence step deterministic. This isolates workflow and integration correctness from model behavior. Phase 10 can introduce AI/RAG behind stable typed interfaces while preserving provenance and safety semantics.

## Safety Boundary

The prototype uses no real PHI and does not diagnose, recommend treatment, determine medical necessity, approve/deny authorization, modify source records, or submit authorization. Human review remains required.

## Outcome

NorthStar Health now has an executable synthetic vertical slice from case intake through structured evidence investigation. Phase 10 will add the AI/RAG/agent layer while preserving these contracts and controls.
