# NorthStar Health — Customer Discovery

## Phase 1 — Customer Discovery

### Project Context

NorthStar Health is a fictional multi-hospital healthcare organization used for this Forward Deployed Engineer portfolio project.

The initial area of investigation is prior authorization operations, with a focus on imaging services such as MRI and CT.

All patients, organizations, workflows, volumes, identifiers, and operational data used in this project are fictional or synthetic. No real protected health information (PHI) is used.

---

## 1. Primary Operational Challenge

Routine prior authorization cases are generally manageable when the required information and documentation are readily available.

The larger operational challenge occurs when a prior authorization becomes an exception.

For imaging orders such as MRI or CT, payers may require supporting clinical evidence including:

- Previous treatment
- Physical therapy
- Medication history
- Previous imaging
- Clinical evaluation
- Other supporting documentation

Required evidence may be distributed across structured EHR data, clinical notes, scanned documents, external medical records, and other systems.

Authorization specialists must manually investigate these sources to determine:

- What the payer requires
- What evidence already exists
- Where the evidence came from
- Whether the evidence is sufficient
- What documentation is missing
- Which team needs to provide missing information

---

## 2. Business and Operational Impact

Prior authorization exceptions can create:

- Additional investigation time for authorization specialists
- Repeated chart review
- Additional communication with physicians and clinical staff
- Case escalations
- Rework
- Delayed authorization submissions
- Potential scheduling delays
- Additional work when incomplete submissions require follow-up
- Potential reimbursement and revenue-cycle impact
- Poorer patient experience when scheduled services are delayed

The problem therefore extends beyond staff productivity and can affect clinical operations, scheduling, revenue-cycle processes, and patient experience.

---

## 3. Primary Users and Stakeholders

### Primary User

**Prior Authorization Specialist**

The authorization specialist is the primary operational user for the initial use case.

### Additional Stakeholders

- Prior Authorization Supervisor
- Physicians
- Nurses
- Medical Assistants
- Scheduling Staff
- Revenue Cycle Staff
- Health Information Management / Records Staff
- IT and Integration Teams
- Security and Compliance Teams
- Patients

---

## 4. Current High-Level Workflow

A typical imaging prior authorization workflow may include:

1. A physician creates an imaging order.
2. The organization determines whether prior authorization is required.
3. An authorization specialist opens or receives the case.
4. The specialist verifies the patient, coverage, procedure, diagnosis, and ordering provider.
5. The specialist determines the payer's authorization requirements.
6. The specialist searches for supporting clinical evidence.
7. Relevant evidence may be found in structured records, clinical notes, previous encounters, medications, imaging history, or external documents.
8. If required evidence is missing or unclear, the specialist contacts the appropriate clinical team.
9. Additional documentation is collected.
10. The authorization package is prepared.
11. The authorization request is submitted to the payer.
12. The payer may approve the request, request additional information, or deny the request.
13. Additional-information requests or denials may create further investigation, escalation, peer-to-peer review, resubmission, or appeal workflows.

A more detailed workflow will be created during Phase 3 — Current-State Workflow Mapping.

---

## 5. Systems Identified During Discovery

Potential systems involved include:

- Electronic Health Record (EHR)
- Scheduling system
- Eligibility and coverage systems
- Payer portals and APIs
- Prior authorization work queue or authorization platform
- Clinical document repositories
- External medical-record sources
- Revenue-cycle systems

The authoritative source for each data element will be defined during Data + System Discovery.

---

## 6. Information Needed by Authorization Specialists

Authorization specialists may need:

- Patient identity
- Insurance coverage
- Payer
- Ordering provider
- Requested procedure
- Procedure code
- Diagnosis
- Scheduled procedure date
- Prior authorization requirement
- Payer documentation requirements
- Clinical history
- Previous treatments
- Physical therapy history
- Medication history
- Previous imaging
- Clinical notes
- Supporting documents
- Previous authorization history
- Current authorization status

---

## 7. Most Difficult Information to Locate

Basic patient, coverage, order, and scheduling information is generally more structured.

The more difficult problem is locating and interpreting clinical evidence required by the payer.

Relevant evidence may be distributed across multiple encounters and documents over an extended period.

For example, answering a question such as:

> Has the patient completed the required period of conservative treatment?

may require reviewing several clinical records rather than querying a single structured field.

---

## 8. Common Exception Categories

Potential prior authorization exceptions include:

- Missing clinical documentation
- Required treatment not documented
- Conflicting information
- Incorrect or inactive coverage
- Unclear payer requirements
- External medical records unavailable
- Incorrect procedure information
- Duplicate authorization
- Expired previous authorization
- Payer request for additional information
- Incomplete clinical notes
- Procedure changed after authorization work began

These categories may later become evaluation and testing scenarios.

---

## 9. Synthetic Operating Assumptions

For portfolio design and testing, NorthStar Health may use synthetic operating assumptions such as:

- Approximately 1,000 imaging orders requiring prior authorization per week
- Approximately 700 routine cases
- Approximately 300 exception cases
- Approximately 100 complex exception cases

These values are fictional portfolio assumptions and are not presented as real healthcare organization statistics.

Baseline distributions and performance targets will be defined later in the project.

---

## 10. Major Source of Manual Effort

The discovery process identified a major source of operational effort:

> Authorization specialists spend significant time searching the clinical record and determining whether evidence required by the payer already exists.

The problem is therefore not simply submitting an authorization request.

A significant challenge is reconstructing the authorization case from fragmented information.

---

## 11. Human Decision Points

Human review remains necessary for:

- Patient and case verification
- Procedure verification
- Payer and coverage verification
- Validation of supporting documentation
- Resolution of ambiguous clinical information
- Resolution of conflicting system information
- Escalation decisions
- Submission decisions governed by organizational policy

AI assistance should support these decisions rather than silently replace required human judgment.

---

## 12. Evidence Provenance Requirement

Users must be able to determine where information presented by the system originated.

Evidence should preserve provenance such as:

- Source system
- Source document
- Encounter
- Document date
- Relevant extracted information
- Retrieval timestamp when appropriate

AI-generated summaries should be traceable to underlying evidence.

---

## 13. Uncertainty and Conflict Handling

The system should not fabricate missing evidence or silently resolve conflicting information.

When evidence is uncertain:

1. The uncertainty should be visible to the user.
2. The system should avoid presenting unsupported conclusions as facts.
3. The case should remain available for human investigation.

When authoritative systems disagree, the conflict should be surfaced for resolution.

---

## 14. Security and Privacy Constraints

The solution will need to consider:

- Authentication
- Role-based access control
- Protection of PHI
- Encryption in transit and at rest
- Audit logging
- Data minimization
- Secrets management
- Access monitoring
- Appropriate retention controls
- AI data boundaries
- Organizational security and compliance requirements

The portfolio implementation will use synthetic data only.

---

## 15. Authoritative Data Sources

Initial discovery suggests the following possible ownership model:

- Patient demographics → EHR
- Clinical documentation → EHR
- Physician orders → EHR
- Appointments → Scheduling system
- Coverage → Eligibility / payer systems
- Prior authorization requirements → Payer
- Authorization status → Authorization system / payer
- Clinical evidence → Original clinical source

This model will be validated and expanded during Phase 4 — Data + System Discovery.

---

## 16. Desired User Experience

The authorization specialist should eventually be able to open a case and quickly understand:

- Who the patient is
- What procedure was ordered
- Which payer covers the patient
- Whether prior authorization is required
- What documentation is required
- What evidence is currently available
- Where that evidence originated
- What documentation appears to be missing
- What action may be required next

---

## 17. Initial Non-Goals

The system should not:

- Diagnose patients
- Replace physicians or other clinical professionals
- Fabricate clinical evidence
- Modify clinical records autonomously
- Silently resolve conflicting patient information
- Present unsupported AI conclusions as established facts
- Automatically submit questionable cases without required review
- Expose patient information to unauthorized users

Detailed system boundaries and non-goals will be refined in later phases.

---

## 18. Failure and Fallback Requirement

AI functionality should not become the only path for processing prior authorization cases.

If AI functionality is unavailable or uncertain, authorized employees should still be able to continue using an appropriate standard workflow.

Human fallback will therefore be treated as a system requirement.

---

## 19. Adoption Requirements

For operational users to adopt the platform, it should:

- Reduce unnecessary manual investigation
- Be reliable
- Make evidence sources visible
- Fit naturally into the existing workflow
- Avoid adding unnecessary operational complexity
- Clearly communicate uncertainty

---

## 20. Initial Success Signals

Potential business outcomes identified during discovery include:

- Reduced manual investigation time
- Faster exception-case resolution
- Reduced unnecessary follow-up
- Reduced avoidable escalation
- Reduced authorization-related scheduling delays
- Improved consistency of case preparation

Formal KPIs, baselines, and targets will be established during Phase 6 — Success Metrics.

---

## 21. Initial Use-Case Scope

The initial implementation will focus on:

**Imaging prior authorization exceptions involving missing or fragmented clinical evidence, initially for MRI and CT workflows.**

The project will not attempt to solve every healthcare prior authorization workflow at once.

This narrow initial scope provides a realistic vertical slice while preserving enterprise integration, workflow, security, data, and AI challenges.

---

## Discovery Summary

NorthStar Health authorization specialists spend significant effort resolving imaging prior authorization exceptions because payer requirements and supporting clinical evidence may be distributed across multiple systems and clinical documents.

Specialists must manually determine what evidence is required, locate relevant evidence, identify missing documentation, coordinate with clinical teams, and prepare cases for submission.

This fragmented investigation process can create operational effort, rework, escalation, and potential scheduling delays.

The discovery phase does not assume that AI alone is the solution. Subsequent phases will define the business problem, map the current-state workflow, investigate systems and data, prioritize use cases, establish measurable success criteria, and determine the appropriate technical architecture.
