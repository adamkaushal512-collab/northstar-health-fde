from dataclasses import dataclass
@dataclass(frozen=True)
class TenantContext:
 tenant_id:str; payer_scope:tuple[str,...]; environment:str
def assert_tenant_access(context:TenantContext,requested_tenant_id:str)->None:
 if context.tenant_id!=requested_tenant_id: raise PermissionError("cross_tenant_access_denied")
