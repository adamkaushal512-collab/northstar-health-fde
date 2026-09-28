# NorthStar Health — Data + System Discovery

## Phase 4 — System Landscape

## 1. Purpose

This document defines the current enterprise system and data landscape supporting the NorthStar Health imaging prior authorization workflow.

The initial use case remains MRI and CT prior authorization exceptions where required clinical evidence is missing, fragmented, inconsistent, or difficult to locate.

The purpose of this phase is to determine:

- which enterprise systems participate in the workflow
- what business responsibility each system owns
- what data each system provides
- which system is authoritative for each major data domain
- how records are identified across systems
- how information can be accessed or exchanged
- how fresh the information must be
- what integration and reliability constraints exist
- what assumptions require customer validation

This is discovery work.

It does not yet define the final solution architecture or implementation.

---

## 2. FDE Discovery Principles

A Forward Deployed Engineer should not begin by connecting every available system.

The first objective is to understand the minimum set of systems and data required to solve the selected business problem.

For the NorthStar Health use case, the critical questions are:

1. Where does an imaging order originate?
2. Where is the scheduled procedure maintained?
3. Where is patient insurance coverage verified?
4. Where is the authorization case managed?
5. Where are payer authorization requirements obtained?
6. Where does supporting clinical evidence live?
7. Which system owns authorization status?
8. How are records correlated across systems?
9. How quickly can each source change?
10. What happens when a source is unavailable or contradictory?

These questions establish the integration boundary for later phases.

---

## 3. Portfolio Assumptions

NorthStar Health is fictional.

The system landscape below represents a realistic enterprise healthcare environment but does not claim that any specific real health system uses this exact architecture.

For portfolio purposes, assume NorthStar Health operates:

- multiple hospitals and outpatient facilities
- centralized imaging authorization operations
- an enterprise EHR
- a scheduling platform
- insurance eligibility capabilities
- a prior authorization work queue
- payer portals and selected payer APIs
- clinical and scanned-document repositories
- internal identity, security, audit, and integration services

All patient and clinical information used later in the project will be synthetic.

Production assumptions would require validation with customer engineering, operations, security, compliance, and application owners.

---

# 4. Enterprise System Landscape

## 4.1 Electronic Health Record — EHR

### Business Responsibility

The EHR is the primary clinical system of record.

It contains information needed to understand why an imaging procedure was ordered and what supporting clinical evidence exists.

### Relevant Data

Examples include:

- patient demographics
- medical record number
- encounters
- ordering provider
- imaging orders
- diagnosis information
- clinical notes
- medication history
- procedures
- previous imaging
- treatment history
- therapy documentation
- clinical observations

### Phase 4 Source-of-Truth Assumption

The EHR is authoritative for:

- clinical orders
- clinical documentation
- encounter history
- recorded diagnoses
- documented treatment evidence

This assumption must be validated with the customer because some supporting documents may reside outside the primary EHR.

### Potential Integration Methods

Depending on customer capabilities:

- FHIR APIs
- vendor APIs
- integration engine feeds
- document interfaces
- event feeds
- controlled database or reporting access

Direct database access should not be assumed.

---

## 4.2 Scheduling System

### Business Responsibility

The scheduling system manages the operational appointment for the MRI or CT procedure.

### Relevant Data

- appointment identifier
- patient identifier
- procedure
- imaging facility
- appointment date
- appointment time
- appointment status
- reschedule status

### Source-of-Truth Assumption

The scheduling system is authoritative for the operational imaging appointment.

### Why It Matters

Authorization urgency depends heavily on the scheduled procedure date.

A technically complete authorization workflow that ignores appointment timing may fail operationally.

---

## 4.3 Eligibility and Coverage System

### Business Responsibility

Provides current insurance eligibility and coverage information.

### Relevant Data

- payer
- insurance plan
- member identifier
- group information
- coverage status
- effective dates
- termination dates

### Source-of-Truth Assumption

The eligibility/coverage service is authoritative for the latest verified coverage result used by the authorization workflow.

The EHR may contain insurance information, but stored EHR coverage data may not represent the latest eligibility verification.

### FDE Concern

Coverage data can change.

The platform must eventually distinguish:

- stored insurance information
- recently verified eligibility
- payer-returned coverage information

---

## 4.4 Prior Authorization Platform / Work Queue

### Business Responsibility

Tracks the operational authorization case.

### Relevant Data

- authorization case ID
- assigned specialist
- case status
- payer
- procedure
- submission status
- operational notes
- escalation state
- follow-up date
- payer reference number
- authorization number when approved

### Source-of-Truth Assumption

The authorization platform is authoritative for NorthStar's internal operational case state.

The payer remains authoritative for the payer's authorization decision.

These are related but different concepts.

---

## 4.5 Payer Systems

Payer interaction may occur through:

- payer portal
- payer API
- clearinghouse
- authorization network
- telephone workflow
- fax workflow

### Business Responsibility

The payer determines:

- whether authorization is required
- applicable authorization requirements
- request status
- requests for additional information
- authorization outcome

### Relevant Data

- authorization requirement
- required documentation
- payer case identifier
- submission status
- request for additional information
- approval
- denial
- authorization number
- effective dates

### Source-of-Truth Assumption

The payer is authoritative for:

- payer-defined authorization requirements
- payer-side case status
- final payer authorization decision

### FDE Concern

Payer integration capability will vary.

Some payers may provide APIs.

Others may still require portal-based or manual workflows.

The solution architecture must not assume uniform payer connectivity.

---

## 4.6 Clinical Document Repository

### Business Responsibility

Stores documents that may not be available as structured EHR data.

Examples:

- scanned clinical records
- external medical records
- faxed documents
- imported reports
- historical documentation

### Relevant Data

- document ID
- patient identifier
- document type
- document date
- source organization
- author when available
- document content
- ingestion timestamp

### Source-of-Truth Consideration

The repository may be authoritative for the stored document artifact, while the clinical meaning remains tied to the originating source.

Provenance must therefore be preserved.

---

## 4.7 External Medical Records

Some required evidence may originate outside NorthStar Health.

Examples include:

- external physical therapy
- previous imaging
- outside specialist notes
- prior treatment records

### FDE Concern

External records may arrive through:

- health information exchange
- electronic document exchange
- fax
- patient-provided records
- manual upload

Availability and structure may vary significantly.

The system must tolerate incomplete external evidence.

---

# 5. Core Data Objects

The following objects represent the minimum information required to support the selected workflow.

---

## 5.1 Patient

Minimum attributes:

- patient_id
- medical_record_number
- name
- date_of_birth

Future implementation should minimize unnecessary patient data.

The project should retrieve only information needed for the workflow.

---

## 5.2 Coverage

Minimum attributes:

- coverage_id
- patient_id
- payer_id
- plan_id
- member_id
- coverage_status
- effective_date
- termination_date
- verification_timestamp

---

## 5.3 Imaging Order

Minimum attributes:

- order_id
- patient_id
- ordering_provider_id
- procedure_code
- procedure_description
- diagnosis_codes
- clinical_indication
- order_date
- order_status

---

## 5.4 Imaging Appointment

Minimum attributes:

- appointment_id
- patient_id
- order_id
- facility_id
- scheduled_datetime
- appointment_status

---

## 5.5 Authorization Case

Minimum attributes:

- authorization_case_id
- patient_id
- order_id
- coverage_id
- payer_id
- assigned_specialist
- case_status
- payer_case_id
- authorization_number
- created_at
- updated_at

---

## 5.6 Payer Requirement

Minimum attributes:

- requirement_id
- payer_id
- plan_id
- procedure_code
- requirement_type
- requirement_description
- effective_date
- source
- source_timestamp

Requirements may include evidence such as:

- clinical examination
- treatment history
- medication history
- physical therapy
- previous imaging
- symptom duration

Payer requirements should eventually retain provenance and version information.

---

## 5.7 Clinical Evidence

Clinical evidence is not necessarily a single database record.

It may be derived from:

- clinical note
- encounter
- observation
- procedure
- medication history
- therapy documentation
- imaging report
- external document

Minimum evidence representation should include:

- evidence_id
- patient_id
- evidence_type
- source_system
- source_record_id
- source_document_id when applicable
- service_date
- author when available
- extracted or referenced content
- retrieval_timestamp

### Critical Design Requirement

Evidence must remain traceable to its source.

An AI-generated summary must never become the authoritative clinical evidence.

---

## 5.8 Authorization Status

Example operational states may include:

- New
- Investigating
- Waiting for Clinical Documentation
- Ready for Submission
- Submitted
- Pending Payer Review
- Additional Information Requested
- Escalated
- Approved
- Denied
- Closed

These are portfolio assumptions and will be refined during workflow and state-machine design.

---

# 6. Cross-System Identity and Record Correlation

Enterprise systems frequently use different identifiers for the same business entity.

Examples:

Patient:

- EHR patient ID
- medical record number
- payer member ID
- authorization platform patient ID

Provider:

- internal provider ID
- NPI
- payer-specific provider identifier

Procedure:

- internal procedure ID
- CPT/HCPCS code
- payer-specific representation

Authorization:

- internal authorization case ID
- payer case ID
- authorization number

A future integration layer must maintain explicit identifier mappings rather than assuming identifiers are interchangeable.

---

# 7. Source-of-Truth Matrix

| Data Domain | Assumed Authoritative Source | Notes |
|---|---|---|
| Patient clinical identity | EHR | Enterprise identity services may also participate |
| Clinical order | EHR | Order changes must be tracked |
| Clinical documentation | EHR / originating repository | Preserve document provenance |
| Imaging appointment | Scheduling system | Operational appointment state |
| Verified coverage | Eligibility service / payer response | May differ from stored EHR insurance |
| Internal authorization workflow | Authorization platform | Operational state |
| Payer requirements | Payer | Requirements may change |
| Payer authorization status | Payer | Internal platform may cache status |
| External clinical document | Originating document source | Preserve source metadata |

This matrix is an initial discovery artifact, not a final architecture decision.

---

# 8. Healthcare Interoperability Considerations

FHIR is a likely interoperability mechanism for selected EHR data, but the project should not assume that every required data element is available through FHIR.

Potentially relevant FHIR resources may include:

- Patient
- Coverage
- ServiceRequest
- Appointment
- Encounter
- Condition
- Observation
- MedicationRequest
- Procedure
- DiagnosticReport
- DocumentReference
- Practitioner
- Organization

Exact resource availability, profiles, search capabilities, extensions, and authorization scopes must be discovered against the customer's EHR implementation.

FHIR should be treated as an integration mechanism, not as the entire architecture.

---

# 9. Data Freshness Requirements

Different data domains require different freshness expectations.

### High Freshness

Examples:

- authorization status
- appointment status
- coverage verification
- procedure changes

Stale information could cause incorrect operational action.

### Moderate Freshness

Examples:

- recently completed clinical documentation
- new external documents
- newly available imaging reports

### Lower Change Frequency

Examples:

- historical treatment documentation
- older clinical records

### FDE Design Principle

Do not apply one caching policy to every data source.

Freshness requirements should be defined by business consequence.

---

# 10. Integration Patterns

The final architecture may use a combination of:

### Request / Response APIs

Useful when the workflow requires current information immediately.

Examples:

- patient lookup
- authorization status
- coverage verification

### Event-Driven Integration

Useful when downstream systems should react to changes.

Examples:

- imaging order created
- appointment changed
- new clinical document available
- authorization status changed

### Batch Integration

Potentially appropriate for:

- reference data
- historical backfill
- analytics
- non-time-sensitive synchronization

### Document Retrieval

Required for unstructured clinical evidence.

### Human Workflow

Some payer and external-record interactions may remain manual.

A production design must support these manual paths rather than pretending every dependency has an API.

---

# 11. Failure and Degradation Scenarios

The future platform must account for failures such as:

- EHR API unavailable
- payer API unavailable
- authorization platform unavailable
- scheduling data delayed
- eligibility verification timeout
- document retrieval failure
- incomplete FHIR response
- stale cached information
- mismatched patient identifiers
- duplicate records
- conflicting procedure information
- payer portal requiring manual action

### FDE Principle

Integration failure must be visible.

The system should not silently convert unavailable information into "no evidence exists."

Those are fundamentally different states.

---

# 12. Data Quality Risks

Potential data-quality issues include:

- missing identifiers
- duplicate patients
- inconsistent procedure codes
- outdated insurance information
- incomplete clinical notes
- delayed document ingestion
- incorrect document classification
- missing service dates
- conflicting diagnosis information
- payer requirement version changes

Later phases should define validation, reconciliation, observability, and human-review behavior for these cases.

---

# 13. Security and Access Discovery

Detailed security architecture will be handled in Phase 8.

However, system discovery must identify access boundaries early.

Questions include:

- Which users may access which patient information?
- Which service accounts can call each API?
- Which EHR scopes are required?
- Which payer credentials are required?
- Which operations require user context?
- Which actions require elevated privileges?
- What data may be logged?
- What data must not appear in application logs?
- What audit events must be captured?
- What retention requirements apply?

The project should follow least-privilege and minimum-necessary principles.

---

# 14. Observability Requirements Discovered Early

Enterprise integrations require operational visibility.

Later implementation should be able to distinguish:

- successful request
- source unavailable
- authentication failure
- authorization failure
- timeout
- malformed response
- incomplete data
- stale data
- mapping failure
- patient correlation failure
- downstream rejection

Without this distinction, operational teams cannot determine whether a case is missing evidence or whether the integration itself failed.

---

# 15. Key Integration Boundaries

For the initial vertical slice, the likely integration boundary is:

EHR
→ imaging order and clinical evidence

Scheduling
→ appointment and urgency

Eligibility / Coverage
→ current coverage

Authorization Platform
→ case workflow

Payer
→ requirements and authorization status

Document Repository
→ supporting unstructured evidence

These six areas form the minimum enterprise landscape required to support the selected use case.

Additional systems should be added only when discovery demonstrates a business requirement.

---

# 16. FDE Discovery Questions for Customer Validation

Before production implementation, an FDE should validate the following with NorthStar stakeholders.

### EHR

- Which EHR vendor and version are used?
- Which FHIR resources are enabled?
- Which APIs require vendor-specific interfaces?
- How are clinical documents retrieved?
- Are event notifications available?
- What rate limits apply?

### Scheduling

- Is scheduling part of the EHR or a separate system?
- What system is authoritative for appointment state?
- How are reschedules and cancellations exposed?

### Coverage

- How is eligibility currently verified?
- How recent must verification be before authorization submission?
- What happens when EHR insurance differs from payer eligibility?

### Authorization Platform

- How are authorization cases created?
- What statuses exist today?
- Is an API available?
- Can external systems update cases?
- What audit history is retained?

### Payers

- Which payers represent the highest imaging authorization volume?
- Which provide APIs?
- Which require portals?
- Where are payer requirements maintained?
- How are requirement changes communicated?

### Clinical Documents

- Which document repositories exist?
- How are external records ingested?
- Is document text searchable?
- Are document types reliable?
- Is provenance retained?

### Security

- What authentication mechanism is used?
- What service-to-service identity model exists?
- What user authorization model applies?
- What audit requirements apply?

### Reliability

- What are source-system SLAs?
- What rate limits exist?
- What downtime patterns occur?
- Which workflows must continue during integration outages?

These questions would normally be answered through customer interviews, architecture reviews, API documentation, sandbox access, and controlled technical experiments.

---

# 17. Phase 4 Technical Decisions

Based on discovery so far, the project will use the following working decisions.

### Decision 1 — Do Not Build a Replacement EHR

NorthStar's clinical systems remain authoritative.

The future platform will integrate with them.

### Decision 2 — Preserve Source Provenance

Clinical evidence must retain:

- source system
- source record
- source document when applicable
- date
- retrieval context

### Decision 3 — Separate Operational State from Payer State

NorthStar's authorization workflow state and the payer's authorization state are related but not identical.

Both must be represented explicitly.

### Decision 4 — Treat Payer Connectivity as Heterogeneous

The architecture must support API-enabled and manual payer workflows.

### Decision 5 — Do Not Treat Missing Data as Negative Evidence

"Evidence not found" is different from "evidence does not exist."

### Decision 6 — Support Human Investigation

The future platform should accelerate investigation without eliminating necessary human review.

### Decision 7 — Prefer Standards Where Practical

FHIR and standard healthcare identifiers should be used where they provide reliable interoperability.

Vendor-specific integration remains acceptable where standards do not expose the required workflow data.

### Decision 8 — Minimize Data Movement

The platform should retrieve and persist only the information required for the operational use case.

---

# 18. What Remains Unknown

An FDE should explicitly track uncertainty rather than hide it.

The following remain unknown because NorthStar Health is fictional and no real customer environment has been connected:

- actual EHR vendor
- exact FHIR capability statement
- API rate limits
- payer API coverage
- authorization platform vendor
- exact document repository
- event availability
- source-system SLAs
- authentication mechanisms
- authorization scopes
- actual case volumes
- actual latency requirements
- exact retention requirements

These will be represented as assumptions until validated or simulated later in the portfolio.

---

# 19. Phase 4 Outcome

Phase 4 establishes the minimum enterprise data and system landscape required for the imaging prior authorization exception workflow.

The critical systems are:

1. EHR
2. Scheduling
3. Eligibility / Coverage
4. Prior Authorization Platform
5. Payer Systems
6. Clinical Document Repository

The primary data objects are:

- Patient
- Coverage
- Imaging Order
- Imaging Appointment
- Authorization Case
- Payer Requirement
- Clinical Evidence
- Authorization Status

The discovery also establishes several architectural constraints:

- systems remain authoritative for their respective domains
- cross-system identifiers require explicit reconciliation
- clinical evidence requires provenance
- data freshness varies by business consequence
- payer connectivity is heterogeneous
- integration failures must be distinguishable from missing data
- human workflows must remain supported
- healthcare standards such as FHIR should be used where practical but should not be assumed to solve every integration requirement

These findings provide the technical foundation for Phase 5 — Use-Case Prioritization and, later, Phase 7 — Solution Architecture.
