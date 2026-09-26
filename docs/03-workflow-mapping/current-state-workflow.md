# NorthStar Health — Current-State Workflow Mapping

## Phase 3 — Current-State Workflow

## 1. Purpose

This document maps the current-state operational workflow for imaging prior authorization exceptions at NorthStar Health before implementation of the proposed platform.

The initial scope focuses on MRI and CT prior authorization cases in which required clinical evidence is missing, fragmented, inconsistent, or difficult to locate.

The purpose of this phase is to understand how work is performed today, including:

- actors involved
- systems used
- handoffs between teams
- decision points
- manual investigation
- waiting states
- exception paths
- operational bottlenecks
- failure points

This document describes the current state only. It does not define the future AI-enabled solution.

---

## 2. Primary Workflow Actors

### 2.1 Prior Authorization Specialist

The Prior Authorization Specialist is the primary operational user.

Responsibilities may include:

- reviewing incoming authorization work
- determining whether prior authorization is required
- identifying payer requirements
- locating supporting clinical evidence
- identifying missing documentation
- communicating with clinical teams
- preparing authorization submissions
- monitoring authorization status
- responding to payer requests for additional information
- escalating unresolved cases

### 2.2 Ordering Physician

The ordering physician determines that an imaging procedure is clinically appropriate and places the order.

The physician may also need to:

- clarify the clinical reason for the procedure
- provide additional documentation
- respond to payer questions
- participate in peer-to-peer review when required

### 2.3 Nurse / Medical Assistant / Clinical Staff

Clinical staff may help locate or provide:

- clinical notes
- treatment history
- medication history
- physical therapy documentation
- previous imaging
- supporting documentation requested by the authorization team

### 2.4 Scheduling Team

The scheduling team manages the imaging appointment and may need authorization status before the procedure can proceed.

They may:

- schedule the MRI or CT
- monitor authorization status
- contact the authorization team
- reschedule or delay appointments when authorization is unresolved

### 2.5 Prior Authorization Supervisor

The supervisor handles difficult or escalated cases.

Examples include:

- unclear payer requirements
- conflicting information
- urgent cases
- repeated payer requests
- unresolved documentation issues
- workflow exceptions

### 2.6 Payer

The payer determines authorization requirements and evaluates submitted information according to its coverage and authorization processes.

Possible payer responses include:

- authorization approved
- additional information requested
- authorization denied
- peer-to-peer review requested
- authorization not required

### 2.7 Patient

The patient is affected by the workflow even though they may not directly participate in the authorization investigation.

Authorization delays can affect:

- appointment timing
- communication
- care coordination
- patient experience

---

## 3. Systems Involved

The current workflow may require users to work across multiple systems.

### Electronic Health Record (EHR)

Contains information such as:

- patient demographics
- physician orders
- diagnosis information
- encounter history
- progress notes
- treatment history
- medication history
- clinical documentation

### Scheduling System

Contains:

- imaging appointment
- facility
- scheduled date
- procedure
- scheduling status

### Eligibility / Coverage System

Used to verify:

- insurance coverage
- payer
- plan
- member information
- eligibility status

### Prior Authorization Platform / Work Queue

Used to:

- manage authorization cases
- track work status
- assign cases
- record operational notes
- track submissions and follow-up

### Payer Portal or Payer API

Used to:

- determine authorization requirements
- review payer-specific instructions
- submit authorization requests
- upload documentation
- check authorization status
- receive requests for additional information

### Document Repository

May contain:

- scanned records
- external medical records
- supporting documents
- faxed documents
- historical records

### Communication Systems

May include:

- secure messaging
- internal task queues
- telephone
- fax
- email where organizational policy permits

These systems support communication between authorization staff, clinical teams, scheduling teams, and external organizations.

---

## 4. Current-State End-to-End Workflow

### Step 1 — Imaging Order Is Created

The ordering physician places an MRI or CT order.

The order may include:

- patient
- procedure
- diagnosis
- ordering provider
- clinical indication

Primary system:

- EHR

Output:

- imaging order

---

### Step 2 — Imaging Appointment Is Scheduled

The scheduling team schedules the requested procedure.

Information may include:

- procedure
- imaging facility
- appointment date
- appointment time

Primary system:

- scheduling system

Output:

- scheduled imaging appointment

Potential issue:

The appointment may be scheduled before the authorization process is fully resolved.

---

### Step 3 — Authorization Case Enters Work Queue

The imaging order is identified as potentially requiring prior authorization.

A case or work item is created or assigned to a Prior Authorization Specialist.

Primary systems:

- authorization platform
- work queue
- EHR

Output:

- authorization case requiring investigation

---

### Step 4 — Specialist Verifies Patient and Coverage Information

The specialist verifies:

- patient identity
- payer
- insurance plan
- member information
- coverage status
- ordering provider
- procedure

Primary systems:

- EHR
- eligibility system
- authorization platform

Decision:

Is coverage information complete and consistent?

If yes:

- continue authorization investigation

If no:

- investigate coverage discrepancy
- contact appropriate operational team
- place case into a waiting or exception state when necessary

---

### Step 5 — Determine Whether Prior Authorization Is Required

The specialist determines whether the requested MRI or CT requires prior authorization.

This may require reviewing:

- payer portal
- payer rules
- authorization platform
- procedure information
- plan information

Decision:

Is prior authorization required?

If no:

- document that authorization is not required
- update the case
- allow downstream scheduling workflow to continue

If yes:

- continue to payer requirement review

---

### Step 6 — Determine Payer Requirements

The specialist identifies what the payer requires for the authorization request.

Requirements may depend on:

- payer
- insurance plan
- procedure
- diagnosis
- clinical indication
- site of service
- previous treatment
- previous imaging

Potential required evidence may include:

- recent clinical notes
- diagnosis documentation
- symptom history
- conservative treatment
- physical therapy
- medication history
- previous imaging
- specialist evaluation

Primary systems:

- payer portal
- payer documentation
- authorization platform

Major current-state difficulty:

Payer requirements may not be represented in a consistent structure across payers.

---

### Step 7 — Search for Supporting Clinical Evidence

The specialist searches the patient's clinical record for evidence required by the payer.

Possible sources include:

- progress notes
- specialist notes
- primary care notes
- therapy notes
- medication history
- imaging history
- procedure history
- scanned documents
- external records

Primary systems:

- EHR
- document repository
- external medical records

This is one of the major manual investigation steps.

The specialist may need to:

1. open multiple encounters
2. read long clinical notes
3. search different sections of the chart
4. compare dates
5. determine whether documentation satisfies a payer requirement
6. record what was found
7. identify what remains missing

---

## 5. Major Decision Point — Is Required Evidence Available?

After reviewing the available clinical record, the specialist determines whether required supporting evidence appears to be available.

### Path A — Evidence Appears Complete

The specialist prepares the authorization request.

Proceed to submission preparation.

### Path B — Evidence Is Missing

The specialist identifies the missing information and contacts the appropriate clinical team.

The case enters an exception workflow.

### Path C — Evidence Is Conflicting or Ambiguous

The specialist cannot confidently determine whether the available documentation satisfies the requirement.

The case may require:

- additional chart review
- clinical clarification
- supervisor review
- payer clarification

This is another exception workflow.

---

## 6. Missing Clinical Evidence Exception Workflow

When required evidence cannot be located, the specialist determines what information is missing.

Examples:

- physical therapy documentation
- duration of conservative treatment
- medication history
- previous imaging results
- recent physician examination
- symptom duration
- specialist evaluation

The specialist then identifies which person or team may provide the missing information.

Possible destinations:

- ordering physician
- nurse
- medical assistant
- clinic staff
- medical records team
- external provider

A request is sent using the available communication workflow.

The authorization case may then enter a waiting state.

---

## 7. Waiting State

While waiting for additional information, the specialist may be unable to continue the authorization request.

Possible waiting conditions include:

- waiting for physician response
- waiting for nurse or medical assistant
- waiting for documentation completion
- waiting for external medical records
- waiting for payer clarification
- waiting for corrected insurance information
- waiting for updated procedure information

During this period:

- the authorization case remains unresolved
- the imaging appointment may approach
- scheduling may request status
- the patient may require updates
- operational urgency may increase

This waiting state is an important source of workflow latency.

---

## 8. Clinical Team Response

The clinical team reviews the request from the authorization specialist.

Possible outcomes:

### Outcome A — Existing Evidence Is Identified

The clinical team points the specialist to existing documentation.

The specialist returns to the chart and reviews it.

### Outcome B — Documentation Is Added

The physician or clinical staff adds or completes required documentation.

The specialist must later return to the case and verify the new information.

### Outcome C — Information Is Still Unavailable

The case remains unresolved and may require escalation.

### Outcome D — Order or Clinical Information Changes

The physician may modify:

- procedure
- diagnosis
- clinical indication
- supporting documentation

The authorization specialist must re-evaluate the case.

---

## 9. Authorization Request Preparation

Once sufficient information appears to be available, the specialist prepares the authorization request.

The specialist may need to:

- confirm patient information
- confirm coverage
- confirm procedure
- confirm diagnosis
- select supporting notes
- upload documentation
- enter payer-required information
- record operational notes

Primary systems:

- EHR
- authorization platform
- payer portal

Manual effort remains high because information may need to be transferred between systems.

---

## 10. Authorization Submission

The request is submitted to the payer.

Possible submission mechanisms include:

- payer portal
- payer API
- authorization platform
- fax
- telephone workflow

The authorization case status is updated.

Example status:

- Submitted / Pending Payer Review

---

## 11. Payer Review

The payer evaluates the submitted request.

Possible outcomes include:

### Approved

Authorization is granted.

The authorization record is updated and scheduling can proceed according to operational policy.

### Additional Information Requested

The payer requests additional clinical information.

The case returns to an evidence investigation workflow.

### Denied

The payer denies the authorization request.

The case may require:

- denial review
- additional documentation
- reconsideration
- appeal
- peer-to-peer review
- physician involvement

### Peer-to-Peer Requested

The payer requests discussion with an appropriate clinician.

The authorization team coordinates the next step according to organizational policy.

---

## 12. Rework Loop

A major characteristic of the current-state workflow is rework.

Example:

Payer requests additional evidence
→ specialist reviews payer request
→ specialist searches EHR
→ evidence not found
→ specialist contacts clinical team
→ waits for response
→ documentation added
→ specialist reviews documentation
→ specialist returns to payer portal
→ additional information submitted
→ waits for payer response

A single authorization case may move through this loop multiple times.

---

## 13. Scheduling Escalation

If authorization remains unresolved while the imaging appointment approaches, scheduling may contact the authorization team.

Possible outcomes include:

- continue waiting
- expedite investigation
- escalate the case
- contact clinical team again
- reschedule appointment
- delay procedure according to organizational policy

This creates additional coordination work across teams.

---

## 14. Current-State Handoffs

Important handoffs include:

### Physician → Scheduling

Imaging order becomes a scheduled procedure.

### Scheduling → Authorization Team

Scheduled imaging requiring authorization enters authorization workflow.

### Authorization Specialist → Clinical Team

Specialist requests missing clinical evidence or clarification.

### Clinical Team → Authorization Specialist

Clinical team provides or identifies documentation.

### Authorization Specialist → Payer

Authorization request and supporting documentation are submitted.

### Payer → Authorization Specialist

Payer returns approval, denial, or request for additional information.

### Authorization Team → Scheduling

Authorization status is communicated so the appointment can proceed or be managed appropriately.

Each handoff introduces the possibility of:

- delay
- incomplete information
- duplicate communication
- lost context
- inconsistent status

---

## 15. Current-State Information Flow

A simplified information flow is:

Physician Order
→ EHR
→ Scheduling
→ Authorization Work Queue
→ Coverage Verification
→ Payer Requirement Review
→ Clinical Evidence Search
→ Missing Evidence Investigation
→ Clinical Team
→ Authorization Specialist
→ Payer Submission
→ Payer Review
→ Authorization Status
→ Scheduling

The workflow is not strictly linear.

Cases may move backward when:

- documentation is missing
- information conflicts
- the payer requests additional evidence
- procedure information changes
- coverage information changes
- clinical clarification is required

---

## 16. Primary Bottlenecks

### 16.1 Manual Clinical Evidence Search

Specialists may need to review multiple notes and encounters to locate required evidence.

### 16.2 Fragmented Systems

Relevant information exists across several systems and interfaces.

### 16.3 Unstructured Documentation

Important evidence may exist inside free-text clinical notes rather than structured fields.

### 16.4 Variable Payer Requirements

Requirements vary by payer, plan, procedure, and clinical scenario.

### 16.5 Missing Documentation

Required information may not yet exist in the chart.

### 16.6 Human Handoffs

Requests between authorization staff and clinical teams introduce waiting time.

### 16.7 Conflicting Information

Procedure, diagnosis, coverage, or other information may differ across systems.

### 16.8 Rework

Payer requests for additional information can send the case back through earlier workflow stages.

### 16.9 Scheduling Deadline Pressure

Unresolved authorization cases become increasingly urgent as appointment dates approach.

---

## 17. Failure Modes

Potential current-state failure modes include:

- required evidence exists but is not found
- outdated documentation is submitted
- incomplete documentation is submitted
- wrong document is selected
- payer requirement is misunderstood
- conflicting information is not noticed
- clinical team request is delayed
- authorization status is not communicated
- duplicate work is performed
- case remains in a queue too long
- appointment approaches without resolved authorization
- payer requests additional information
- case requires repeated rework

These are workflow risks to investigate and measure later.

---

## 18. Human Judgment Points

Human judgment is currently required when:

- determining whether documentation satisfies a payer requirement
- interpreting ambiguous clinical evidence
- identifying relevant information in long notes
- resolving conflicting information
- deciding whether additional clarification is required
- determining escalation path
- preparing documentation for submission
- responding to payer requests
- handling unusual exceptions

Future automation must preserve appropriate human review at these points.

---

## 19. Current-State Workflow Summary

The current imaging prior authorization exception workflow requires the Prior Authorization Specialist to coordinate information across:

- EHR
- scheduling
- coverage systems
- authorization work queues
- payer portals
- document repositories
- clinical teams

The most operationally difficult cases are not straightforward authorization cases.

They are exception cases where the specialist must reconstruct the case from fragmented information, determine payer requirements, locate supporting clinical evidence, identify missing or conflicting information, coordinate with other teams, and repeatedly revisit the case as new information becomes available.

The workflow contains multiple:

- system transitions
- manual searches
- decision points
- handoffs
- waiting states
- rework loops

These characteristics create the operational foundation for the next phases of the project.

---

## 20. Phase 3 Outcome

The current-state workflow is now mapped from imaging order creation through payer response and downstream scheduling coordination.

The mapping identifies the major operational problem areas:

1. fragmented information
2. manual evidence retrieval
3. variable payer requirements
4. missing documentation
5. conflicting information
6. human handoffs
7. waiting states
8. payer-driven rework
9. scheduling deadline pressure

These findings will inform Phase 4 — Data + System Discovery, where the project will identify the specific enterprise systems, interfaces, data objects, ownership boundaries, integration constraints, and source-of-truth responsibilities required to support the workflow.
