# NorthStar Health — Use-Case Prioritization

## Phase 5 — Use-Case Prioritization

## 1. Purpose

NorthStar Health's prior authorization workflow contains many possible opportunities for automation and operational improvement.

Attempting to solve the entire prior authorization lifecycle in the first deployment would create unnecessary integration complexity, safety risk, organizational dependency, and difficulty measuring whether the solution creates value.

The purpose of this phase is therefore to select a focused initial vertical slice that:

- addresses a meaningful operational problem
- can be integrated into the existing workflow
- has identifiable enterprise data sources
- benefits from AI-assisted information retrieval
- preserves appropriate human decision-making
- can be evaluated with measurable outcomes
- provides a realistic path toward broader deployment

This reflects an FDE principle:

> Start with a narrow, high-value workflow that can be deployed and measured before expanding the platform.

---

## 2. Candidate Use Cases

Based on customer discovery, workflow mapping, and system discovery, the following opportunities were identified.

### Candidate A — Clinical Evidence Investigation

Help Prior Authorization Specialists locate, organize, and review clinical evidence required for MRI/CT authorization exceptions.

Examples:

- physical therapy history
- medication history
- previous imaging
- symptom duration
- conservative treatment
- specialist evaluation
- relevant clinical notes

### Candidate B — Payer Requirement Retrieval

Help specialists identify payer-specific authorization requirements for a procedure.

### Candidate C — Coverage Discrepancy Investigation

Help identify inconsistencies between stored insurance information and current eligibility results.

### Candidate D — Authorization Status Monitoring

Track payer authorization status and surface cases requiring follow-up.

### Candidate E — Scheduling Risk Identification

Identify unresolved authorization cases approaching their scheduled imaging date.

### Candidate F — Denial / Appeal Assistance

Help organize information required after an authorization denial.

---

## 3. Prioritization Criteria

The candidate use cases are evaluated against criteria relevant to an enterprise FDE deployment.

### Business Impact

Does the use case address meaningful operational effort, delay, or rework?

### Workflow Frequency

Does the problem occur often enough to justify investment?

### User Pain

Does the workflow create significant friction for the primary user?

### Data Availability

Can the required information reasonably be obtained from identified enterprise systems?

### Technical Feasibility

Can an initial implementation be built without requiring every enterprise integration to be solved first?

### AI Suitability

Can AI provide useful assistance without becoming the authoritative clinical or coverage decision-maker?

### Human Oversight

Can important decisions remain under human control?

### Safety and Compliance Risk

Can the use case be implemented without giving AI inappropriate clinical or coverage authority?

### Measurability

Can the organization determine whether the deployment improves the workflow?

### Expansion Potential

Can the initial capability become a foundation for additional workflows later?

---

## 4. Qualitative Prioritization

| Candidate | Business Impact | Technical Feasibility | AI Suitability | Human Oversight | Measurability | Initial Priority |
|---|---|---|---|---|---|---|
| Clinical Evidence Investigation | High | High | High | Strong | High | Selected |
| Payer Requirement Retrieval | High | Medium | Medium | Strong | High | Later |
| Coverage Discrepancy Investigation | Medium | Medium | Low-Medium | Strong | Medium | Later |
| Authorization Status Monitoring | Medium | High | Low | Strong | High | Later |
| Scheduling Risk Identification | Medium | High | Low | Strong | High | Later |
| Denial / Appeal Assistance | High | Medium | Medium-High | Required | Medium | Later |

The table represents portfolio prioritization assumptions rather than measured production results.

Actual prioritization in a customer deployment would be validated using operational volume, cycle-time data, error rates, user interviews, integration feasibility, security review, and implementation cost.

---

## 5. Selected Initial Use Case

The selected initial vertical slice is:

**AI-assisted clinical evidence investigation for MRI and CT prior authorization exceptions involving missing, fragmented, or difficult-to-locate supporting evidence.**

The primary user remains the:

**Prior Authorization Specialist**

The platform will help the specialist answer:

1. What evidence does this authorization case require?
2. What relevant evidence exists in available clinical records?
3. Where did that evidence come from?
4. What required information appears to be missing?
5. Is available information conflicting or uncertain?
6. What should the specialist investigate next?

The system assists the investigation.

The human remains responsible for reviewing the evidence and taking the appropriate operational action.

---

## 6. Why This Use Case Was Selected

### 6.1 It Directly Addresses the Core Workflow Bottleneck

Phase 3 identified manual clinical evidence search as one of the most significant sources of operational effort.

Specialists may need to open multiple encounters, review long notes, compare dates, search document repositories, and determine whether relevant evidence exists.

The selected use case attacks that bottleneck directly.

### 6.2 It Has a Clear User

The Prior Authorization Specialist has a concrete task:

**reconstruct enough of the clinical evidence picture to prepare or advance the authorization case.**

A clearly defined user reduces ambiguity during product design and evaluation.

### 6.3 AI Has a Useful but Bounded Role

The workflow involves:

- retrieval
- extraction
- summarization
- evidence organization
- provenance
- missing-information detection
- conflict surfacing

These capabilities are appropriate areas for AI assistance.

The AI does not need authority to:

- diagnose the patient
- determine treatment
- independently determine medical necessity
- approve coverage
- deny coverage
- override payer policy

This creates a safer initial AI boundary.

### 6.4 Human Review Naturally Fits the Workflow

Authorization specialists already investigate and review clinical information.

The system can therefore operate as an investigation copilot rather than replacing the user.

### 6.5 Relevant Data Sources Have Already Been Identified

Phase 4 identified likely evidence sources including:

- EHR
- clinical notes
- encounters
- document repositories
- external records

This gives the project a realistic technical path toward implementation.

### 6.6 Provenance Can Be Made Explicit

Every surfaced evidence item can retain:

- source system
- source record
- source document
- service date
- author when available
- retrieval timestamp

This allows users to verify AI-assisted findings against authoritative records.

### 6.7 The Outcome Can Be Measured

Potential metrics include:

- investigation time per exception case
- number of records manually opened
- time to identify missing evidence
- repeat clinical-team requests
- authorization preparation cycle time
- percentage of AI-surfaced evidence with valid provenance
- user acceptance of surfaced evidence

Exact targets will be defined in Phase 6.

---

## 7. Initial Vertical Slice

The first implementation should intentionally remain narrow.

### Trigger

An MRI or CT authorization case requires clinical evidence investigation.

### Inputs

Minimum expected inputs include:

- patient identifier
- imaging order
- procedure
- diagnosis / clinical indication
- payer
- payer evidence requirements
- available clinical records

### Processing

The future platform will:

1. identify relevant payer evidence requirements
2. retrieve potentially relevant clinical information
3. associate evidence with requirements
4. preserve source provenance
5. identify apparently missing information
6. surface conflicting or uncertain information
7. present findings to the specialist

### Output

A unified investigation view containing:

- authorization case context
- evidence requirements
- supporting evidence
- source references
- missing evidence
- conflicts / uncertainty
- suggested investigation areas

### Human Action

The Prior Authorization Specialist reviews the findings and decides the appropriate operational next step.

---

## 8. Explicit Non-Goals for the Initial Slice

The first vertical slice will not:

- autonomously submit authorization requests
- approve or deny authorization
- determine medical necessity independently
- make clinical recommendations
- modify the clinical record
- fabricate missing evidence
- silently resolve conflicting information
- automatically appeal denials
- replace payer portals
- replace the EHR
- support every specialty and procedure
- eliminate human review

These boundaries reduce initial deployment risk and keep the implementation measurable.

---

## 9. Deferred Use Cases

The following capabilities remain valuable but are intentionally deferred.

### Payer Requirement Automation

Potential future capability once payer data quality and integration patterns are better understood.

### Coverage Investigation

Potential future capability requiring stronger eligibility integration and reconciliation logic.

### Authorization Status Automation

Useful operational capability but does not address the primary evidence-investigation bottleneck.

### Scheduling Risk Management

Could later use authorization status and appointment timing to identify cases at risk of delay.

### Denial and Appeal Support

Potentially high value but introduces additional workflow complexity and should follow validation of the initial investigation capability.

Deferring these capabilities prevents the first deployment from becoming an oversized platform project.

---

## 10. Expansion Path

If the initial use case demonstrates value, the platform can expand incrementally.

A possible sequence is:

Clinical Evidence Investigation
→ Payer Requirement Intelligence
→ Authorization Case Preparation
→ Status Monitoring
→ Scheduling Risk Management
→ Denial / Appeal Assistance
→ Additional Procedures and Specialties

Expansion should depend on measured value and customer demand rather than being assumed in advance.

---

## 11. FDE Deployment Principle

The goal of the initial deployment is not maximum feature coverage.

The goal is to prove that NorthStar Health can improve a specific operational workflow while maintaining:

- human control
- source traceability
- security
- reliability
- measurable business value

A successful first deployment should create evidence for whether the platform deserves broader investment.

---

## 12. Phase 5 Decision

NorthStar Health will prioritize:

**AI-assisted clinical evidence investigation for MRI/CT prior authorization exceptions.**

This use case is selected because it combines:

- meaningful operational pain
- a clearly identified user
- identifiable enterprise data
- a bounded AI role
- strong human oversight
- measurable workflow outcomes
- realistic technical feasibility
- expansion potential

The next phase will define the success metrics and evaluation criteria required to determine whether this use case actually improves the authorization workflow.

---

## 13. Phase 5 Outcome

Phase 5 narrows the broader prior authorization opportunity into one deployable initial vertical slice.

The project will proceed with:

**MRI/CT prior authorization exception investigation focused on finding, organizing, and tracing required clinical evidence for a human Prior Authorization Specialist.**

Phase 6 — Success Metrics will define how operational value, AI quality, provenance, safety, reliability, and user adoption will be measured.
