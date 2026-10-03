# NorthStar Health — Security, Privacy & Governance

## Phase 8 — Security, Privacy & Governance

## 1. Purpose

This document defines the security, privacy, and AI-governance controls for NorthStar Health's initial vertical slice:

**AI-assisted clinical evidence investigation for MRI/CT prior authorization exceptions.**

Phase 7 established the technical architecture. Phase 8 defines the trust boundaries and controls that must govern that architecture before implementation.

This is a public portfolio design using synthetic data. It does not claim that a real healthcare deployment is compliant merely because these controls are documented. A production deployment would require customer security, privacy, legal, compliance, risk, and vendor review.

---

## 2. Security Objectives

The initial deployment must protect:

- patient confidentiality
- clinical-data integrity
- authorization-case integrity
- enterprise credentials
- payer information
- audit evidence
- AI-system boundaries
- service availability

The design follows these principles:

- least privilege
- minimum necessary access
- defense in depth
- explicit trust boundaries
- secure defaults
- auditable access
- data minimization
- fail-safe behavior
- human accountability
- separation of authoritative and AI-derived information

---

## 3. Data Classification

The platform should classify information before deciding how it may be accessed, persisted, logged, or transmitted.

### Restricted Healthcare Data

Examples:

- patient identifiers
- clinical notes
- diagnoses
- medications
- procedures
- imaging history
- authorization case details linked to a patient
- payer/member identifiers

Treat this information as highly sensitive and potentially PHI in a real deployment.

### Confidential Operational Data

Examples:

- internal workflow configuration
- payer integration configuration
- operational metrics
- system architecture
- non-public runbooks

### Secrets

Examples:

- API keys
- OAuth client secrets
- database credentials
- signing keys
- service-account credentials

Secrets must never be committed to source control or included in prompts, logs, fixtures, or documentation.

### Public / Synthetic Portfolio Data

Only synthetic, non-identifying test data is allowed in the public repository.

---

## 4. Trust Boundaries

The primary trust path is:

```text
Prior Authorization Specialist
        │
        ▼
Authenticated Application
        │
        ▼
Authorization / RBAC
        │
        ▼
Investigation Service
        │
        ├──────────────► Audit / Telemetry
        │
        ▼
Controlled Orchestration Layer
        │
        ├──────────────► AI Provider Boundary
        │
        ▼
Enterprise Integration Adapters
        │
        ▼
EHR / Documents / Scheduling / Coverage / PA / Payer
```

Each transition is a security boundary.

Identity, authorization, data minimization, validation, and audit requirements apply at those boundaries.

---

## 5. Authentication

Production users must authenticate through an enterprise-approved identity provider.

Preferred approaches include:

- OIDC
- OAuth 2.0
- SAML-backed enterprise SSO where required

The application should not create an independent password store when enterprise identity is available.

Authentication establishes identity.

It does not by itself grant access to patient information.

---

## 6. Authorization and RBAC

Authorization must be enforced server-side.

Potential roles include:

### Prior Authorization Specialist

May:

- investigate assigned or permitted cases
- view required evidence
- review AI-assisted findings
- accept/reject evidence suggestions
- record workflow feedback

### PA Supervisor

May additionally:

- review escalated cases
- review selected operational metrics
- inspect workflow exceptions within permitted scope

### Integration Service

May access only the source APIs required for the workflow.

### Security / Audit Role

May inspect security and audit metadata under approved policy without automatically receiving unrestricted clinical-content access.

### System Administrator

Administrative capability must not imply unrestricted clinical access.

RBAC should be combined with contextual authorization where necessary, such as assignment, facility, region, or organizational scope.

---

## 7. Least Privilege

Every human and service identity receives only the permissions necessary for its task.

Examples:

- EHR adapter receives read access only to required clinical resources
- scheduling adapter receives only required appointment access
- AI component cannot directly query the EHR
- observability service does not receive full clinical documents
- CI/CD credentials cannot read production clinical data
- developers do not receive production PHI by default

Permissions should be reviewable and revocable.

---

## 8. Minimum Necessary Data

The investigation workflow should retrieve only information reasonably required for the authorization task.

The system should avoid:

- bulk patient-record replication
- unrelated clinical-history retrieval
- sending entire longitudinal records to an LLM when targeted evidence is sufficient
- copying full clinical documents into logs
- retaining source content indefinitely

Retrieval should be constrained by patient, case, evidence requirement, source type, and relevant time range when possible.

---

## 9. PHI Handling

In a real deployment, protected clinical information must remain inside approved processing boundaries.

Controls should include:

- approved data flows
- encrypted transport
- approved storage
- explicit retention
- controlled access
- auditability
- vendor review
- contractual safeguards where required
- secure deletion processes

The portfolio implementation uses synthetic data only.

No real PHI should appear in:

- Git history
- GitHub Issues
- pull requests
- screenshots
- test fixtures
- logs
- model prompts used for public demonstrations
- documentation

---

## 10. Encryption

### In Transit

Use TLS for service-to-service and user-to-service communication.

### At Rest

Persisted sensitive information must use approved encryption-at-rest controls.

### Key Management

Encryption keys should be managed through an approved key-management service rather than embedded in application code.

Application secrets and encryption keys must remain separate.

---

## 11. Secrets Management

Secrets must be supplied at runtime through an approved secrets mechanism.

Examples:

- cloud secrets manager
- workload identity
- CI/CD secret store
- local environment variables for development

The repository should include only examples such as:

```text
EHR_API_URL=
EHR_CLIENT_ID=
AI_PROVIDER_ENDPOINT=
```

Never real secret values.

Recommended repository protections include:

- `.gitignore`
- secret scanning
- pre-commit scanning where practical
- CI secret scanning

A leaked secret must be rotated, not merely deleted from the latest commit.

---

## 12. Enterprise Service Identity

Adapters should authenticate to enterprise systems using dedicated workload identities when supported.

Avoid:

- shared human credentials
- hard-coded tokens
- long-lived static credentials where short-lived identity is available

Each adapter's permissions should reflect its actual integration requirement.

---

## 13. AI Provider Boundary

Clinical content must not be sent to an external model provider merely because an API is technically available.

Before real healthcare data crosses that boundary, NorthStar Health would need to validate:

- approved vendor status
- contractual requirements
- data-use terms
- retention behavior
- training/data-reuse behavior
- geographic processing requirements
- security controls
- incident obligations
- supported privacy configuration
- customer legal/compliance requirements

The architecture must allow the AI provider to be replaced without redesigning enterprise integrations.

---

## 14. Prompt Data Minimization

The AI layer should receive the smallest context sufficient for its task.

Instead of automatically sending an entire chart, the workflow should prefer:

```text
payer requirement
+ relevant case context
+ retrieved candidate evidence
+ provenance metadata
```

Prompt construction is therefore part of the security boundary.

---

## 15. Prompt Injection and Untrusted Clinical Content

Clinical documents and external payer content must be treated as untrusted data.

A note, scanned document, imported record, or payer text could contain instructions that should never control the AI system.

The system must distinguish:

```text
SYSTEM / DEVELOPER POLICY
        │
        ▼
AUTHORIZED TOOL POLICY
        │
        ▼
WORKFLOW INSTRUCTIONS
        │
        ▼
UNTRUSTED RETRIEVED CONTENT
```

Retrieved content must not be allowed to redefine:

- system policy
- permissions
- allowed tools
- authorization scope
- data destinations
- guardrails

---

## 16. Tool Security

The LLM does not receive arbitrary tool execution.

Every tool should have:

- explicit purpose
- typed input schema
- typed output schema
- authorization checks
- patient/case scope
- bounded operations
- timeout
- audit event
- safe error behavior

Initial tools should be read-oriented.

State-changing operations should be deferred until independently justified, secured, tested, and approved.

---

## 17. Input Validation

All external inputs require validation.

Examples:

- patient IDs
- authorization IDs
- payer IDs
- procedure codes
- dates
- document identifiers
- pagination tokens
- tool arguments

Typed schemas should reject malformed or unexpected data before it reaches downstream systems.

---

## 18. Output Validation

AI output should not be trusted merely because it matches natural language expectations.

Before presentation, validate:

- schema
- evidence references
- required provenance
- allowed status values
- source availability state
- prohibited action fields
- unsupported factual claims where detectable

Invalid output should fail closed to a safe result such as:

**AI analysis unavailable — manual review required.**

---

## 19. Provenance Security

Provenance is both a product requirement and a security control.

Every case-supporting evidence item should link to a permitted source reference.

The platform must prevent:

- cross-patient evidence leakage
- stale source references being represented as current
- AI-created fake document identifiers
- references to records the user is not authorized to view

Source links must pass authorization checks when accessed.

---

## 20. Patient and Case Isolation

Every retrieval request should be scoped to the intended patient and authorization case.

The platform must test for:

- cross-patient retrieval
- cross-case leakage
- incorrect identifier mapping
- cached data leakage
- vector-search tenant/patient leakage

Semantic retrieval must not bypass patient or organizational filters.

---

## 21. Vector and Embedding Security

If embeddings or vector storage are introduced:

- only approved data may be embedded
- patient/tenant isolation must be enforced
- metadata filters must be applied before or during retrieval
- deletion/retention requirements must extend to embeddings
- embedding stores must not become uncontrolled clinical-data replicas
- access must be audited where appropriate

An embedding is still derived from sensitive information and should be governed accordingly.

---

## 22. Logging Policy

Logs should be useful without becoming a shadow clinical database.

Preferred log fields include:

- correlation ID
- request ID
- service
- operation
- source system
- result category
- latency
- error category
- timestamp

Avoid logging:

- full clinical notes
- full prompts containing PHI
- full model responses containing clinical content
- credentials
- access tokens
- unnecessary patient identifiers

Where identifiers are operationally necessary, use approved minimization or pseudonymous references.

---

## 23. Audit Logging

Security and workflow audit records should capture important events such as:

- user initiated investigation
- patient/case scope resolved
- source queried
- access denied
- source failed
- evidence surfaced
- AI analysis executed
- specialist accepted/rejected evidence
- specialist correction recorded
- administrative configuration changed

Audit events should include:

- actor or service identity
- action
- target reference
- timestamp
- outcome
- correlation ID

Audit records should be protected against unauthorized modification.

---

## 24. Data Retention

Different data categories require different retention policies.

Examples:

### Source Clinical Content

Prefer retrieval from the authoritative source rather than unnecessary long-term duplication.

### Investigation Metadata

Retain according to operational, audit, legal, and customer requirements.

### AI-Derived Summaries

Retain only when justified and governed.

### Prompts / Model Responses

Do not retain by default merely for convenience. Retention must have an explicit purpose and approved policy.

### Logs

Use defined retention and avoid sensitive payloads.

Retention periods are customer/legal decisions and are intentionally not invented in this portfolio.

---

## 25. Secure Deletion

When data reaches the end of its approved retention period, deletion must cover relevant copies including:

- primary storage
- caches
- derived artifacts
- embeddings where applicable
- temporary files
- approved backup lifecycle

Deletion requirements should be documented and testable.

---

## 26. Caching Security

Caches must not weaken authorization.

Controls include:

- patient/case-aware cache keys
- tenant isolation
- expiration
- encryption where required
- no shared response caching across unauthorized users
- invalidation for high-consequence stale data

Authorization must be evaluated appropriately even when data is served from cache.

---

## 27. Network Security

A production deployment should restrict network paths so components communicate only with required dependencies.

Potential controls include:

- private networking
- firewall/security-group rules
- egress restrictions
- service-to-service authentication
- API gateways
- allow-listed enterprise endpoints

The AI service should not receive unrestricted network access merely because it uses tools.

---

## 28. API Security

The investigation API should enforce:

- authenticated requests
- authorization
- request-size limits
- schema validation
- rate limiting where appropriate
- safe error messages
- correlation IDs
- audit events
- transport encryption

Internal APIs are not automatically trusted merely because they are internal.

---

## 29. Error Handling and Information Disclosure

Errors returned to users should be operationally useful without exposing:

- credentials
- stack traces
- internal network details
- sensitive source payloads
- hidden model instructions

Detailed diagnostic information belongs in protected observability systems.

---

## 30. Dependency and Supply-Chain Security

Implementation should include:

- pinned or controlled dependencies
- dependency vulnerability scanning
- container scanning
- minimal container images
- software inventory where practical
- review of AI SDKs and integration libraries
- controlled build pipeline

Production images should be built through CI rather than manually modified after deployment.

---

## 31. Repository Security

The public portfolio repository must remain synthetic and secret-free.

Controls should include:

- branch-based development
- pull requests
- `.gitignore`
- secret scanning
- dependency scanning
- CI checks
- no production configuration
- no real patient data
- no customer credentials

Security-sensitive examples should use placeholders.

---

## 32. CI/CD Security Boundary

CI/CD should have only the permissions necessary to build, test, scan, and deploy approved artifacts.

Avoid:

- broad permanent cloud credentials
- production PHI in CI
- secrets printed to build logs
- deployment from unreviewed branches

Where supported, prefer short-lived workload identity over static credentials.

---

## 33. Environment Separation

Development, test, staging, and production should be logically separated.

Development uses synthetic data.

Production credentials and data must not be copied into development merely to simplify testing.

Configuration should identify environment explicitly.

---

## 34. AI Safety Boundaries

The AI system must not:

- fabricate clinical evidence
- present unsupported content as verified evidence
- hide known conflicts
- convert retrieval failure into evidence absence
- diagnose patients
- recommend treatment
- determine medical necessity independently
- autonomously approve or deny authorization
- bypass required human review
- execute arbitrary enterprise actions

These restrictions should be enforced through architecture, permissions, schemas, guardrails, and evaluation rather than prompt wording alone.

---

## 35. Human Accountability

The Prior Authorization Specialist remains accountable for reviewing the investigation output and taking the operational next step.

The UI should clearly distinguish:

- source evidence
- AI-derived summary
- AI-derived requirement mapping
- missing-evidence flag
- uncertainty
- system/source failure

Users should not have to infer which information came from AI.

---

## 36. Model Governance

Every production model configuration should have identifiable metadata such as:

- provider
- model/version
- deployment identifier
- configuration version
- prompt/workflow version
- evaluation version
- release date
- approved use case

A model upgrade is a controlled change, not an invisible dependency update.

---

## 37. Prompt and Workflow Versioning

Prompts and orchestration logic affect system behavior and should be version-controlled.

Changes should be:

- reviewed
- tested
- evaluated
- traceable to a release

Production incidents should be diagnosable against the exact workflow/model configuration used.

---

## 38. Model Change Management

Before changing the production model or material prompt behavior:

1. run the evaluation suite
2. compare against the current approved baseline
3. inspect safety regressions
4. inspect evidence/provenance regressions
5. review latency/cost impact
6. approve the release through the defined process

A newer model is not automatically a safer or better production model.

---

## 39. Evaluation Governance

The evaluation set should include:

- straightforward cases
- missing evidence
- conflicting evidence
- irrelevant notes
- duplicate documents
- stale data
- source outages
- identifier mismatches
- prompt-injection content
- ambiguous evidence

Evaluation data must be governed just like application data.

For the public portfolio, evaluation cases are synthetic.

---

## 40. Security Testing

The implementation should eventually test:

- authentication failures
- authorization failures
- cross-patient access attempts
- malformed identifiers
- invalid tool arguments
- prompt injection
- source-system failure
- poisoned/untrusted document instructions
- provenance manipulation
- missing source references
- secret leakage
- unsafe AI action attempts

Security testing belongs in automated testing where practical.

---

## 41. Threat Model

Key threat categories include:

### Unauthorized Clinical Access

A user or service accesses patient information outside permitted scope.

### Cross-Patient Data Leakage

Evidence from one patient appears in another patient's investigation.

### Credential Compromise

A leaked secret allows unauthorized system access.

### Prompt Injection

Retrieved content attempts to redirect the model or trigger unauthorized actions.

### Hallucinated Evidence

The model creates unsupported clinical facts.

### Provenance Spoofing

AI output references nonexistent or incorrect source records.

### Excessive Data Exposure

More clinical data is retrieved, persisted, logged, or transmitted than necessary.

### Stale Data

Old eligibility, appointment, order, or payer information is treated as current.

### Integration Failure Misinterpretation

A source outage is represented as absence of evidence.

### Supply-Chain Compromise

A dependency, image, build system, or package introduces malicious behavior.

---

## 42. Threat-to-Control Mapping

| Threat | Primary Controls |
|---|---|
| Unauthorized clinical access | SSO, RBAC, contextual authorization, audit |
| Cross-patient leakage | case scoping, identifier validation, retrieval filters, tests |
| Credential compromise | secrets manager, short-lived identity, rotation |
| Prompt injection | untrusted-content boundary, tool allow-list, deterministic policy |
| Hallucinated evidence | provenance requirement, evaluation, output validation |
| Provenance spoofing | source-reference validation, adapter verification |
| Excessive exposure | minimum necessary retrieval, retention controls |
| Stale data | freshness metadata, cache policy, source-of-truth rules |
| Integration failure confusion | explicit source status and degraded modes |
| Supply-chain compromise | dependency/image scanning, controlled CI builds |

---

## 43. Incident Response Requirements

A production deployment needs an incident process for:

- unauthorized access
- suspected data exposure
- credential leakage
- incorrect cross-patient retrieval
- unsafe AI behavior
- source integration compromise
- audit-log failure

The platform should provide enough correlation and audit metadata to reconstruct relevant activity.

Incident-response ownership and notification obligations are customer-specific and must be defined before production.

---

## 44. Security Observability

Security-relevant telemetry should include:

- authentication failures
- authorization denials
- unusual access patterns
- source access failures
- tool-policy violations
- malformed requests
- repeated patient-scope failures
- guardrail rejections
- secret-scanning findings
- dependency vulnerabilities

Alert thresholds should be tuned during pilot and production operations.

---

## 45. Privacy-by-Design Decisions

The architecture adopts the following privacy decisions:

1. use synthetic data in the public project
2. retrieve rather than broadly replicate clinical records
3. minimize prompt context
4. separate source evidence from AI interpretation
5. avoid clinical payloads in general application logs
6. govern derived data and embeddings
7. use explicit retention policies
8. keep AI provider boundaries replaceable
9. preserve human review
10. expose source availability and uncertainty

---

## 46. Governance Ownership

A real deployment requires clear ownership.

### Clinical / Operations

Owns workflow appropriateness and user procedures.

### Security

Owns security architecture, vulnerability management, access-control requirements, and incident processes.

### Privacy / Legal / Compliance

Owns applicable privacy obligations, contractual requirements, retention, and approved data use.

### Engineering / FDE

Owns implementation of approved controls, integration behavior, technical auditability, testing, and operational instrumentation.

### AI / Model Governance

Owns approved models, evaluation gates, change management, and use-case boundaries.

No single engineering team should unilaterally declare a healthcare AI deployment compliant.

---

## 47. Production Readiness Security Gates

Before production, verify at minimum:

- enterprise authentication integrated
- authorization rules tested
- least-privilege service identities configured
- real secrets removed from code and configuration
- encryption controls approved
- AI provider/data-processing boundary approved
- PHI logging reviewed
- retention approved
- audit events validated
- cross-patient isolation tested
- prompt-injection defenses evaluated
- provenance controls tested
- model/evaluation version recorded
- incident process established
- fallback workflow verified
- security review completed

A failed critical gate blocks production even if model-quality metrics are strong.

---

## 48. Portfolio Implementation Requirements

The upcoming implementation phases must demonstrate these controls in a realistic synthetic environment.

At minimum, the portfolio should eventually include:

- synthetic healthcare fixtures
- typed request/response schemas
- role-aware access logic
- adapter boundaries
- provenance validation
- source-status handling
- safe logging
- environment-based secrets
- prompt-injection tests
- cross-patient isolation tests
- AI safety evaluations
- audit events
- CI security checks
- documented failure modes

This converts Phase 8 from a policy document into engineering requirements.

---

## 49. Security Architecture Decisions

### SEC-1 — Synthetic Data Only in Public Repository

No real PHI or customer data is permitted.

### SEC-2 — Enterprise Identity Over Local Passwords

Use approved SSO/identity in production.

### SEC-3 — Server-Side Authorization

UI visibility is not an access-control mechanism.

### SEC-4 — Minimum Necessary Retrieval

Do not retrieve the entire chart by default.

### SEC-5 — No Direct LLM Enterprise Access

All access flows through controlled, authorized tools.

### SEC-6 — Treat Retrieved Content as Untrusted

Documents cannot redefine system policy or tool permissions.

### SEC-7 — Provenance Required for Supporting Evidence

Unsupported model text cannot become verified case evidence.

### SEC-8 — Separate AI Interpretation from Source Records

Derived content must remain distinguishable.

### SEC-9 — Safe Failure Over Fabricated Completion

Unavailable data produces an explicit degraded state.

### SEC-10 — Model Changes Require Evaluation

Provider/model/prompt changes are controlled releases.

### SEC-11 — Avoid Sensitive Payload Logging

Observability should rely on metadata wherever possible.

### SEC-12 — Security Gates Can Block Deployment

Workflow speed improvements do not override critical security failures.

---

## 50. Phase 8 Outcome

NorthStar Health now has an explicit security, privacy, and AI-governance model for the initial MRI/CT prior authorization evidence-investigation workflow.

The design establishes:

- data classification
- trust boundaries
- authentication
- RBAC and contextual authorization
- least privilege
- minimum necessary access
- PHI handling principles
- encryption requirements
- secrets management
- workload identity
- AI-provider governance
- prompt minimization
- prompt-injection defenses
- tool security
- input/output validation
- provenance controls
- patient/case isolation
- vector/embedding governance
- safe logging
- audit requirements
- retention and deletion principles
- cache and network security
- API security
- supply-chain controls
- environment separation
- AI safety boundaries
- model and prompt versioning
- evaluation governance
- threat modeling
- incident-response requirements
- production security gates

Phase 8 converts the architecture's trust assumptions into concrete implementation requirements.

The project is now ready for:

**Phase 9 — Rapid Prototype**

The prototype will implement the smallest end-to-end synthetic vertical slice that demonstrates the architecture: case intake, synthetic source adapters, canonical context, evidence retrieval, provenance, bounded AI-assisted analysis, guardrails, and a structured investigation result.
