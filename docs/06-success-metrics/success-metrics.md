# NorthStar Health — Success Metrics

## Phase 6 — Success Metrics

## 1. Purpose

Phase 5 selected the initial NorthStar Health vertical slice:

**AI-assisted clinical evidence investigation for MRI/CT prior authorization exceptions involving missing, fragmented, or difficult-to-locate clinical evidence.**

Phase 6 defines how NorthStar Health will determine whether that capability creates measurable value.

The evaluation must measure more than model quality.

A successful enterprise AI deployment must demonstrate improvement across:

- operational workflow
- evidence retrieval quality
- provenance and traceability
- safety
- reliability
- user adoption
- business outcomes

All numerical targets in this portfolio are initial pilot hypotheses. They are not production results and must be validated against customer baseline data.

---

## 2. Measurement Principles

NorthStar Health will follow several measurement principles.

### Measure the Workflow, Not Only the Model

A technically strong AI system is not useful if Prior Authorization Specialists still spend the same amount of time investigating cases.

Operational outcomes therefore remain primary.

### Establish a Baseline First

Before evaluating improvement, the team must measure the current workflow.

Baseline measurements should include:

- investigation time
- number of records manually reviewed
- evidence-request frequency
- rework
- case preparation time
- user effort

### Preserve Human Review

AI recommendations are assistance, not authoritative clinical or coverage decisions.

Success does not mean eliminating human review.

### Measure Safety Separately

A system can improve speed while still being unsafe.

Safety and provenance therefore have explicit acceptance criteria.

### Segment Results

Metrics should be analyzed by relevant dimensions such as:

- payer
- procedure type
- exception type
- evidence requirement
- source system

Aggregate averages must not hide poor performance in important workflow segments.

---

## 3. North-Star Workflow Metric

The primary workflow metric is:

**Median clinical-evidence investigation time per MRI/CT prior authorization exception.**

This measures the time required for a Prior Authorization Specialist to understand the evidence state of a case sufficiently to determine the next operational action.

The initial hypothesis is that AI assistance should materially reduce investigation time without reducing evidence quality, provenance, or safety.

The exact improvement target will be finalized after baseline measurement.

---

## 4. Operational Metrics

### Investigation Time

Measure:

- median investigation time
- 75th percentile investigation time
- 90th percentile investigation time

Percentiles are important because complex exception cases may be hidden by averages.

### Manual Record Review

Measure the number of clinical records or documents manually opened by the specialist during investigation.

Desired direction:

**Decrease**

### Time to Identify Missing Evidence

Measure the time from investigation start until the specialist can identify required evidence that appears to be unavailable.

Desired direction:

**Decrease**

### Repeat Clinical-Team Requests

Measure how often the authorization team must repeatedly contact clinical staff because the initial evidence request was incomplete or incorrect.

Desired direction:

**Decrease**

### Rework Rate

Measure cases requiring repeated evidence investigation because relevant information was missed, incorrectly interpreted, or insufficiently traced.

Desired direction:

**Decrease**

### Case Preparation Cycle Time

Measure elapsed time from the start of evidence investigation to the point at which the case is ready for the next authorization workflow step.

Desired direction:

**Decrease**

---

## 5. AI Evidence Quality Metrics

The AI capability must be evaluated against a human-reviewed reference dataset constructed from synthetic or appropriately approved test cases.

### Evidence Retrieval Recall

Of the evidence items determined by expert review to be relevant, what percentage did the system surface?

This is particularly important because missing relevant evidence may cause unnecessary rework or delay.

### Evidence Precision

Of the evidence surfaced by the system, what percentage is actually relevant to the authorization requirement?

Low precision increases user review burden.

### Requirement-to-Evidence Matching Accuracy

Measure whether the system correctly associates clinical evidence with the payer requirement it is intended to support.

### Missing-Evidence Detection

Measure whether the system correctly identifies requirements for which sufficient evidence was not found in the accessible records.

The system must distinguish:

**Evidence not found**

from:

**Evidence does not exist**

### Conflict Detection

Measure whether known contradictory or inconsistent information is surfaced to the user rather than silently resolved.

### Summary Faithfulness

Evaluate whether generated summaries accurately represent the retrieved source material without introducing unsupported clinical facts.

---

## 6. Provenance Metrics

Every evidence item used by the AI should remain traceable to an authoritative source.

### Provenance Coverage

Measure the percentage of surfaced evidence items containing sufficient source metadata for human verification.

Initial pilot target:

**100% of evidence presented as case-supporting evidence must include source provenance.**

Required provenance should include, when available:

- source system
- source record or document
- service or document date
- author or originating organization
- retrieval timestamp

### Source-Link Validity

Measure whether provenance references resolve to the intended source record.

### Unsupported Evidence Rate

Measure evidence claims presented as factual support without an accessible source.

Initial pilot acceptance criterion:

**0 known unsupported evidence claims presented as verified evidence.**

---

## 7. Safety Metrics

Safety requirements are release gates rather than optimization targets.

### Fabricated Clinical Evidence

The system must not invent clinical evidence.

Pilot acceptance criterion:

**0 known fabricated evidence items in the evaluated release set.**

### Autonomous Clinical Decisions

The system must not independently diagnose patients or recommend treatment.

Acceptance criterion:

**No autonomous clinical decision capability.**

### Autonomous Coverage Decisions

The system must not independently approve or deny authorization.

Acceptance criterion:

**No autonomous approval or denial capability.**

### Conflict Suppression

Known conflicting evidence must not be silently converted into a single definitive fact.

### Missing-Data Behavior

Unavailable systems, retrieval failures, or missing records must not be represented as proof that clinical evidence does not exist.

---

## 8. Human Oversight Metrics

### Human Review Coverage

Cases using AI-assisted evidence investigation must retain the required human review step.

Initial target:

**100% for the initial vertical slice.**

### Evidence Acceptance Rate

Measure the percentage of AI-surfaced evidence items accepted by specialists as useful and relevant.

### Correction Rate

Measure how frequently specialists must correct:

- extracted evidence
- requirement mappings
- missing-evidence flags
- summaries

### Override / Rejection Reasons

Capture structured reasons when users reject AI output.

This creates feedback for evaluation and future system improvement.

---

## 9. Reliability Metrics

### Investigation Service Availability

Measure availability of the AI-assisted investigation capability separately from core clinical systems.

The existing authorization workflow must remain usable if the AI capability is unavailable.

### Retrieval Failure Rate

Measure failures when accessing required source systems.

### Processing Latency

Measure time from investigation request to presentation of useful evidence results.

Latency should be evaluated against user workflow expectations rather than an arbitrary model benchmark.

### Degraded-Mode Visibility

Measure whether users are clearly informed when:

- a source system is unavailable
- retrieval is incomplete
- data may be stale
- AI processing fails

Silent degradation is unacceptable.

---

## 10. User Adoption Metrics

### Active Usage

Measure the percentage of eligible exception investigations in which specialists use the AI-assisted workflow.

### Repeat Usage

Measure whether specialists continue using the capability after initial exposure.

### User-Reported Usefulness

Collect structured feedback on whether the capability:

- reduces search effort
- improves case understanding
- makes missing information clearer
- improves confidence in evidence provenance

### Workflow Abandonment

Measure cases where users start the AI-assisted workflow but abandon it and return to fully manual investigation.

Abandonment reasons should be captured.

---

## 11. Business Outcome Metrics

The initial deployment should eventually connect workflow improvements to broader operational outcomes.

Potential measures include:

- authorization preparation throughput
- staff time spent per exception
- avoidable scheduling delays
- repeated patient or clinical-team contacts
- operational cost per investigated exception
- authorization-related rework

These outcomes should not be attributed to AI without appropriate baseline and pilot comparison data.

---

## 12. Initial Pilot Scorecard

The following scorecard defines the initial evaluation structure.

| Dimension | Metric | Desired Direction / Gate |
|---|---|---|
| Workflow | Median investigation time | Decrease |
| Workflow | Manual records opened | Decrease |
| Workflow | Repeat evidence requests | Decrease |
| AI Quality | Evidence retrieval recall | Increase |
| AI Quality | Evidence precision | Increase |
| AI Quality | Requirement-to-evidence accuracy | Increase |
| AI Quality | Summary faithfulness | High |
| Provenance | Evidence provenance coverage | 100% target |
| Provenance | Unsupported verified evidence | 0 known cases |
| Safety | Fabricated clinical evidence | 0 known cases |
| Safety | Autonomous clinical decisions | Not permitted |
| Safety | Autonomous coverage decisions | Not permitted |
| Human Oversight | Required human review | 100% |
| Reliability | Retrieval failures surfaced | Required |
| Reliability | AI outage blocks core workflow | No |
| Adoption | Eligible-case usage | Increase during pilot |
| Adoption | User-reported usefulness | Positive trend |

Exact quantitative performance thresholds should be established using baseline data and pilot validation rather than fabricated for the portfolio.

---

## 13. Pilot Evaluation Design

A future pilot should compare AI-assisted investigations with an appropriate baseline.

For each eligible case, capture:

- case type
- procedure
- payer
- exception category
- investigation start/end time
- evidence requirements
- evidence surfaced
- evidence accepted/rejected
- missing evidence identified
- corrections
- retrieval failures
- final operational next step

The pilot should include both straightforward and difficult exception cases.

Evaluation should include known edge cases such as:

- missing documentation
- conflicting documentation
- stale information
- unavailable source systems
- irrelevant clinical notes
- duplicate records
- incomplete payer requirements

---

## 14. Go / No-Go Framework

Progression beyond the initial pilot requires evidence across multiple dimensions.

A production decision should consider:

1. Does the workflow become meaningfully easier or faster?
2. Is relevant evidence surfaced with acceptable quality?
3. Is every supporting evidence item traceable?
4. Are hallucination and unsupported-evidence controls effective?
5. Are conflicts and missing information represented correctly?
6. Does required human oversight remain intact?
7. Does the system fail safely when dependencies are unavailable?
8. Do specialists find the capability useful enough to continue using it?

No single model-quality metric is sufficient for production readiness.

Safety and provenance failures may block progression even when workflow metrics improve.

---

## 15. FDE Measurement Responsibility

An FDE is responsible for connecting technical system behavior to customer outcomes.

For NorthStar Health, this means instrumenting the workflow so the team can answer:

- Did the deployment reduce operational effort?
- Did users actually adopt it?
- Did retrieval quality remain acceptable?
- Can every important AI claim be traced?
- Where does the system fail?
- Which integrations cause operational problems?
- Are humans correcting the same failure patterns repeatedly?
- Is the system creating measurable value without introducing unacceptable risk?

The purpose of measurement is not to produce impressive dashboard numbers.

It is to determine whether the deployed system deserves continued use, modification, expansion, or rollback.

---

## 16. Phase 6 Decision

NorthStar Health will evaluate the initial AI capability using a multi-layer measurement framework covering:

- workflow efficiency
- AI evidence quality
- provenance
- safety
- human oversight
- reliability
- adoption
- business outcomes

The primary workflow metric will be:

**Median clinical-evidence investigation time per MRI/CT prior authorization exception.**

Safety, provenance, and human-review requirements will operate as deployment gates rather than metrics that can be traded away for speed.

---

## 17. Phase 6 Outcome

NorthStar Health now has:

- a defined initial vertical slice
- a primary workflow metric
- supporting operational metrics
- AI quality metrics
- provenance requirements
- safety gates
- human-oversight measures
- reliability measures
- adoption measures
- a pilot evaluation structure
- a go/no-go framework

The project is now ready for:

**Phase 7 — Solution Architecture**

Phase 7 will translate the selected workflow and measurement requirements into a concrete enterprise architecture, including system boundaries, integration paths, AI components, data flows, security boundaries, human-review points, and failure behavior.
