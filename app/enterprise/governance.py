REQUIRED_ENTERPRISE_CONTROLS={
 "tenant_isolation","rbac","audit_logging","data_retention","model_governance",
 "incident_response","business_continuity","security_review"
}
def governance_gaps(enabled_controls:set[str])->set[str]:
 return REQUIRED_ENTERPRISE_CONTROLS-enabled_controls
