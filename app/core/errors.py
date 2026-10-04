class NorthStarError(Exception):
 code="northstar_error"
class DependencyUnavailable(NorthStarError):
 code="dependency_unavailable"
class InvalidConfiguration(NorthStarError):
 code="invalid_configuration"
