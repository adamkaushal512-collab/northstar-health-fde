# NorthStar Health — AI Evaluation

## Phase 11

Phase 11 adds a repeatable evaluation harness for the MRI/CT prior-authorization evidence-investigation workflow. It moves the project from "the prototype appears to work" to explicit, version-controlled measurements against expected outcomes.

## Evaluation priorities

The initial safety and quality contract measures:

1. requirement-status accuracy
2. evidence provenance
3. grounded summaries
4. preservation of mandatory human review
5. bounded tool execution

The initial dataset is synthetic and deterministic. It is a regression baseline, not a claim about production clinical-model performance.

## Scenarios

**Partial evidence:** PT and examination evidence exist; medication evidence does not.

**Complete evidence:** all three evidence categories exist.

**No matching evidence:** an unrelated record exists but must not satisfy any payer requirement.

## Metrics

- **Requirement accuracy:** expected versus returned requirement statuses.
- **Provenance accuracy:** retrieved evidence with valid source-system and source-record references.
- **Grounding accuracy:** summaries backed by evidence IDs.
- **Human-review rate:** cases retaining `human_review_required=true`.
- **Tool-sequence accuracy:** cases using the approved bounded tool sequence.
- **Pass rate:** cases satisfying the complete baseline contract.

Because this is a small controlled baseline, the required result is 100%. Probabilistic model thresholds will be introduced when a model-backed synthesizer is evaluated.

## Reproducibility

Run:

```bash
python -m app.evals.runner
```

The runner emits machine-readable JSON with per-case and aggregate results. The baseline is also executed by pytest.

## FDE relevance

Evaluation is an operational release contract connecting customer requirements, architecture, AI behavior, regressions, and deployment decisions. New production or pilot failure modes should become new evaluation cases.

## Phase 11 outcome

The repository now contains a version-controlled evaluation dataset, executable scoring harness, aggregate metrics, and regression tests.

Phase 12 will introduce adversarial **Red Team / Safety Testing** designed to make the system violate these guarantees.
