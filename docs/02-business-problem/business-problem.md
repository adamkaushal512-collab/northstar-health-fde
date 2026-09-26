# NorthStar Health — Business Problem Definition

## Phase 2 — Business Problem

### Context

NorthStar Health is a fictional multi-hospital healthcare organization used for this Forward Deployed Engineer portfolio project.

The initial problem area identified during customer discovery is imaging prior authorization, with an initial focus on MRI and CT authorization exceptions.

All patients, organizations, identifiers, workflows, volumes, and operational data used in this project are fictional or synthetic. No real protected health information (PHI) is used.

---

## 1. Current-State Business Problem

NorthStar Health can process many routine imaging prior authorization cases through existing operational workflows.

The larger operational problem occurs when a prior authorization becomes an exception because required information is missing, fragmented, inconsistent, unclear, or difficult to locate.

For an imaging order such as an MRI or CT, an authorization specialist may need to determine:

- Whether prior authorization is required
- Which payer requirements apply
- What clinical documentation is required
- Whether the required evidence exists
- Where that evidence is located
- Whether available evidence is sufficient
- What information is missing
- Which team should provide missing information
- Whether conflicting information requires investigation

The information required to answer these questions may be distributed across multiple enterprise systems and clinical documents.

As a result, authorization specialists may need to manually reconstruct the authorization case before it can proceed.

---

## 2. Problem Statement

NorthStar Health authorization specialists spend significant operational effort resolving imaging prior authorization exceptions because payer requirements and supporting clinical evidence may be distributed across multiple systems, encounters, and clinical documents.

Specialists must manually determine what evidence is required, locate relevant evidence, validate its source, identify missing or conflicting information, coordinate with clinical teams, and prepare the case for the next authorization step.

This fragmented investigation process can create unnecessary manual effort, inconsistent case preparation, repeated communication, escalation, rework, and authorization-related scheduling delays.

---

## 3. Primary User Problem

The primary user for the initial workflow is the Prior Authorization Specialist.

The specialist currently lacks a unified operational view that clearly presents:

- Patient and case context
- Requested imaging procedure
- Coverage and payer
- Applicable authorization requirements
- Required clinical evidence
- Evidence currently available
- Evidence provenance
- Missing documentation
- Conflicting information
- Current case status
- Appropriate next operational step

The specialist therefore spends time reconstructing this information manually.

---

## 4. Root Causes

### 4.1 Fragmented Data

Relevant information may exist across:

- Electronic Health Record (EHR)
- Clinical notes
- Scheduling systems
- Eligibility and coverage systems
- Payer systems
- Prior authorization platforms
- Document repositories
- External medical records

No single source necessarily contains the complete operational picture.

### 4.2 Unstructured Clinical Evidence

Some information required for authorization may exist inside narrative clinical documentation rather than structured fields.

Examples may include:

- Conservative treatment
- Physical therapy
- Medication trials
- Symptoms
- Previous treatment response
- Clinical evaluations

Locating this information may require manual review of multiple documents.

### 4.3 Variable Payer Requirements

Authorization requirements may vary by payer, procedure, plan, and clinical context.

The specialist must determine which requirements apply before evaluating whether the case contains sufficient documentation.

### 4.4 Missing Documentation

Required clinical evidence may not exist in the available record or may not yet have been provided.

This can trigger additional communication with physicians, nurses, medical assistants, records teams, or external organizations.

### 4.5 Conflicting Information

Different systems may contain inconsistent information.

Examples could include:

- Different procedure information
- Coverage discrepancies
- Changed orders
- Duplicate authorization records
- Expired authorization information

These conflicts require explicit investigation rather than silent resolution.

### 4.6 Operational Handoffs

Exception cases may move between authorization specialists, clinical teams, scheduling, supervisors, and other operational groups.

Each handoff can introduce waiting time and additional coordination.

---

## 5. Business Consequences

### Operational Impact

- Increased manual investigation
- Repeated chart review
- Rework
- Additional case handling
- Increased escalation
- Inconsistent case preparation

### Clinical Workflow Impact

- Additional requests to physicians and clinical staff
- Repeated requests for documentation
- Interruptions to existing clinical workflows

### Scheduling and Patient Experience Impact

- Authorization may remain unresolved as the scheduled service approaches
- Scheduling teams may need additional follow-up
- Procedures may require rescheduling when authorization is incomplete
- Patients may experience additional communication or uncertainty

### Revenue-Cycle Impact

- Incomplete documentation can create additional authorization work
- Denials or requests for additional information may require rework
- Delayed authorization can affect downstream revenue-cycle processes

---

## 6. Target Business Outcome

NorthStar Health wants to reduce the operational effort required to resolve imaging prior authorization exceptions while maintaining human oversight, evidence traceability, security, and appropriate clinical and operational controls.

The target future state should help authorized users more quickly understand:

1. What authorization case they are handling
2. What the payer requires
3. What relevant evidence exists
4. Where that evidence originated
5. What information appears to be missing
6. Whether information conflicts across systems
7. What operational action may be required next

The goal is not simply to automate authorization decisions.

The goal is to make exception investigation more efficient, consistent, traceable, and operationally manageable.

---

## 7. Initial Scope

The initial project scope is:

**Imaging prior authorization exceptions involving missing or fragmented clinical evidence, initially focused on MRI and CT workflows.**

The first vertical slice will concentrate on the investigation and case-preparation workflow rather than attempting to automate the entire healthcare prior authorization lifecycle.

---

## 8. In-Scope Capabilities

The initial solution may eventually support capabilities such as:

- Unified prior authorization case view
- Retrieval of relevant case information from connected systems
- Payer requirement representation
- Clinical evidence retrieval
- Evidence provenance
- Missing-document identification
- Conflict detection
- Case summarization
- Human review
- Operational escalation
- Audit logging
- Workflow status tracking

These capabilities are potential solution areas and do not imply that every capability will require AI.

---

## 9. Out of Scope

The initial project will not attempt to:

- Diagnose patients
- Recommend medical treatment
- Replace physicians or other clinical professionals
- Make autonomous clinical decisions
- Determine medical necessity independently
- Automatically approve or deny insurance coverage
- Fabricate missing clinical evidence
- Modify source clinical records autonomously
- Silently resolve conflicting patient or procedure information
- Automatically submit questionable cases without required review
- Replace every prior authorization workflow across all specialties
- Use real patient PHI for portfolio development

---

## 10. Constraints

The solution must account for enterprise healthcare constraints including:

- Sensitive healthcare data
- Authentication and authorization
- Role-based access control
- Auditability
- Data minimization
- Encryption
- System availability
- Legacy systems
- External payer dependencies
- Incomplete data
- Conflicting data
- Human review requirements
- AI uncertainty
- Operational fallback
- Integration reliability

AI functionality must not become the only path for processing a case.

---

## 11. Key Assumptions to Validate

Several assumptions remain unverified and should be tested in later phases:

- Clinical evidence search is a major source of manual effort
- Relevant evidence can be retrieved from accessible source systems
- Payer requirements can be represented in a usable structured form
- Evidence provenance can be preserved throughout the workflow
- Authorization specialists benefit from a unified case workspace
- AI-assisted retrieval can improve evidence discovery without creating unacceptable risk
- Human review can be incorporated without eliminating the operational benefit
- Existing systems expose sufficient integration mechanisms
- The workflow can degrade safely when AI or external services are unavailable

These assumptions are not treated as established facts.

---

## 12. Initial Hypothesis

If NorthStar Health can provide authorization specialists with a unified, traceable view of payer requirements, available clinical evidence, missing information, and system conflicts, then specialists may be able to resolve imaging prior authorization exceptions with less manual investigation and more consistent case preparation.

AI-assisted retrieval and summarization may contribute to this outcome where appropriate, but the project will evaluate those capabilities rather than assume their effectiveness.

---

## 13. Success Direction

Detailed metrics and targets will be defined during Phase 6 — Success Metrics.

Potential success dimensions include:

- Reduced manual investigation time
- Reduced time to prepare exception cases
- Reduced unnecessary chart review
- Reduced repeated documentation requests
- Reduced avoidable escalation
- Improved consistency of case preparation
- Reduced authorization-related scheduling delays
- High evidence provenance coverage
- Safe handling of uncertain or conflicting information
- Reliable human fallback

No numerical improvement claims are made at this stage.

---

## 14. FDE Framing

This project is not framed as:

> Build an AI system for healthcare prior authorization.

It is framed as:

> Improve the operational process for resolving imaging prior authorization exceptions by understanding the workflow, integrating fragmented enterprise information, preserving evidence provenance, supporting human decision-making, and applying AI only where it provides measurable and appropriately controlled value.

This keeps the project centered on the customer's business problem rather than a predetermined technology.

---

## Phase 2 Outcome

The business problem has been narrowed from the broad domain of prior authorization to a specific operational problem:

**Authorization specialists must manually reconstruct imaging prior authorization exception cases from fragmented payer requirements and clinical evidence.**

The next phase will map the current-state workflow in detail, including actors, systems, decision points, handoffs, failure paths, waiting states, and operational bottlenecks.
