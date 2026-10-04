# Phase 16 — Deployment / Environment Strategy

NorthStar is packaged as a containerized FastAPI service with explicit local, development, staging, and production configuration boundaries.

The repository includes a Dockerfile, Docker Compose local workflow, `.dockerignore`, and non-secret environment templates. Real credentials and PHI must never be committed. Production secrets belong in a managed secret store supplied by the deployment platform.

Promotion follows dev → staging → production. The same application artifact should be promoted between environments; environment-specific behavior comes from configuration, not source-code forks.

The current portfolio deployment remains synthetic and single-service. Real EHR/payer connectivity, IAM, managed secrets, ingress/TLS, durable stores, and platform-specific autoscaling are deployment integrations, not simulated claims.
