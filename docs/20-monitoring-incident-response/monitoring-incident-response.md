# Phase 20 — Monitoring + Incident Response

Post-launch operations monitor service health, dependency health, safety regressions, fallback volume, investigation outcomes, latency, and availability.

The incident model distinguishes safety regressions, service outages, and dependency degradation. Safety regressions are highest severity and require rollback/escalation. Dependency degradation activates existing fallback behavior rather than being mistaken for missing clinical evidence.

Availability is represented as an SLO check. In a real deployment these signals would feed an observability backend, dashboards, alert routing, and on-call processes. The portfolio defines the contracts without pretending those external systems are deployed.
