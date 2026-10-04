# Phase 15 — CI/CD + Observability

Phase 15 introduces an automated GitHub Actions quality gate and lightweight observability primitives.

Pull requests and main-branch changes install the project and run the complete pytest suite. Runtime observability includes structured JSON logs with request correlation IDs, counters for operational metrics, and timed spans that can later be connected to OpenTelemetry/export infrastructure.

The portfolio implementation intentionally stops short of pretending a production telemetry backend exists. The interfaces establish where enterprise logging, metrics, tracing, dashboards, and alerts attach.
