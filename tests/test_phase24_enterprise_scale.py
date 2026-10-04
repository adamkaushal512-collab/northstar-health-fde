import pytest
from app.enterprise.tenancy import TenantContext,assert_tenant_access
from app.enterprise.capacity import required_workers
from app.enterprise.governance import governance_gaps,REQUIRED_ENTERPRISE_CONTROLS
def test_cross_tenant_access_denied():
 with pytest.raises(PermissionError):assert_tenant_access(TenantContext("health-a",("payer-a",),"prod"),"health-b")
def test_capacity_includes_headroom():
 assert required_workers(10,2,0.30)==7
def test_governance_complete_only_when_controls_present():
 assert governance_gaps(set())==REQUIRED_ENTERPRISE_CONTROLS
 assert governance_gaps(REQUIRED_ENTERPRISE_CONTROLS)==set()
