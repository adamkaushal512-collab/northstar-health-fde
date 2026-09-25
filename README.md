# NorthStar Health — AI Prior Authorization & Clinical Operations Platform

An enterprise-style Forward Deployed Engineer (FDE) portfolio project focused on improving healthcare prior authorization operations.

## Project Overview

NorthStar Health is a fictional multi-hospital healthcare organization.

The project investigates how fragmented systems, payer requirements, clinical documentation, and manual investigation contribute to operational complexity in prior authorization workflows.

The initial use case focuses on:

**Imaging prior authorization exceptions involving missing or fragmented clinical evidence, initially for MRI and CT workflows.**

## Initial Problem Area

Authorization specialists may need to investigate information across multiple systems and clinical documents to determine:

- What documentation a payer requires
- What clinical evidence already exists
- Where that evidence originated
- What information is missing
- Which team should provide missing information
- Whether a case is ready for the next operational step

The project will explore how enterprise integration, workflow orchestration, structured data, AI-assisted evidence retrieval, human review, security controls, and observability can support this workflow.

## FDE Lifecycle

The project will be developed through an end-to-end Forward Deployed Engineering lifecycle:

1. Customer Discovery
2. Business Problem Definition
3. Current-State Workflow Mapping
4. Data + System Discovery
5. Use-Case Prioritization
6. Success Metrics
7. Solution Architecture
8. Security, Privacy & Governance
9. Rapid Prototype
10. Data / RAG / Agent Build
11. AI Evaluation
12. Red Team / Safety Testing
13. Guardrails + Human Fallback
14. Production Engineering
15. CI/CD + Observability
16. Pilot
17. Production Launch
18. User Adoption
19. Business KPI / ROI
20. Optimization
21. Reusable Patterns
22. Product / Research Feedback
23. Final Portfolio Packaging + Demo

## Current Status

**Phase 1 — Customer Discovery**

Discovery has identified imaging prior authorization exception handling as the initial problem area.

Detailed discovery notes are available at:

`docs/01-customer-discovery/discovery-notes.md`

## Data and Privacy

NorthStar Health is fictional.

All patients, organizations, identifiers, clinical records, payer information, operational metrics, and other data created for this project will be synthetic.

No real protected health information (PHI) should be stored in this repository.

## Engineering Principle

This project does not begin with the assumption that AI is the solution.

The workflow, business problem, systems, data, constraints, security requirements, success criteria, and failure modes will be established before selecting and implementing the final technical approach.
