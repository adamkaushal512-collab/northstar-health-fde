# Phase 14 — Production Engineering

NorthStar now adds production-shaped service primitives: environment configuration, standardized operational errors, bounded retry behavior, request correlation context, and dependency readiness checks.

A live process is not necessarily a ready service. Readiness represents whether required dependencies are available. Transient network/timeout failures receive bounded retries; exhausted attempts become an explicit dependency-unavailable condition rather than an infinite wait.

These controls build directly on Phase 13: dependency failure can be distinguished from missing clinical evidence and safely routed to fallback behavior.
