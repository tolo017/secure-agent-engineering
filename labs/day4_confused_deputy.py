"""
SURFNET AGENT
Day 4: Confused Deputy Laboratory

This laboratory uses fake customer records.
The vulnerable version deliberately demonstrates
an authorization design failure.
"""

from dataclasses import dataclass


# -------------------------------------------------
# 1. SIMULATED CRM DATABASE
# -------------------------------------------------

TENANT_RECORDS = {
    "tenant_A": [
        {"id": "A101", "name": "Amina"},
        {"id": "A102", "name": "Brian"},
    ],

    "tenant_B": [
        {"id": "B201", "name": "David"},
        {"id": "B202", "name": "Grace"},
    ],
}


# -------------------------------------------------
# 2. AUTHENTICATED IDENTITIES
# -------------------------------------------------

@dataclass(frozen=True)
class Principal:
    user_id: str
    tenant_id: str
    roles: frozenset[str]
    scopes: frozenset[str]


SUPPORT_USER = Principal(
    user_id="user_alice",
    tenant_id="tenant_A",
    roles=frozenset({"support"}),
    scopes=frozenset({"crm:read"}),
)


WORK_AGENT = Principal(
    user_id="surfnet-work-agent",
    tenant_id="tenant_A",
    roles=frozenset({"business_agent"}),
    scopes=frozenset({
        "crm:read",
        "crm:write_note",
    }),
)


SECURITY_AGENT = Principal(
    user_id="surfnet-security-agent",
    tenant_id="tenant_A",
    roles=frozenset({"security_agent"}),
    scopes=frozenset({
        "security:read_events",
        "security:create_finding",
    }),
)


PLATFORM_SECURITY_ADMIN = Principal(
    user_id="platform_security_admin",
    tenant_id="surfnet_platform",
    roles=frozenset({"platform_security_admin"}),
    scopes=frozenset({"security:admin"}),
)


# -------------------------------------------------
# 3. TOOL REQUEST
# -------------------------------------------------

@dataclass(frozen=True)
class ToolRequest:
    action: str
    requested_tenant_id: str | None = None
    record_limit: int = 5
    approval_reference: str | None = None


# -------------------------------------------------
# 4. AUTHORIZATION ERROR
# -------------------------------------------------

class AuthorizationDenied(Exception):
    """Raised when an action is not authorized."""
    pass


# -------------------------------------------------
# 5. CRM SERVICE
# -------------------------------------------------

class CRMService:

    # DELIBERATELY VULNERABLE VERSION
    # --------------------------------

    def vulnerable_execute(self, request: ToolRequest):

        """
        The vulnerable service uses its own broad
        authority and trusts the requested tenant ID.

        It does not check who is making the request.
        """

        if request.action != "crm.read_customers":
            raise ValueError("Unsupported action")

        tenant_id = request.requested_tenant_id

        if tenant_id not in TENANT_RECORDS:
            raise ValueError("Unknown tenant")

        return TENANT_RECORDS[tenant_id][
            :request.record_limit
        ]


    # SECURE VERSION
    # --------------------------------

    def secure_execute(
        self,
        request: ToolRequest,
        principal: Principal,
    ):

        """
        The secure version uses the authenticated
        principal supplied by the application.

        It does not trust tenant selection from
        the AI agent or user.
        """

        if request.action not in {
            "crm.read_customers",
            "crm.export_customers",
        }:
            raise AuthorizationDenied(
                "Unsupported CRM action"
            )

        # Tenant identity must come from the
        # authenticated principal, not the AI prompt.

        if request.requested_tenant_id is not None:
            raise AuthorizationDenied(
                "Agent cannot select a tenant"
            )

        # Enforce reasonable operation limits.

        if not 1 <= request.record_limit <= 5:
            raise AuthorizationDenied(
                "Invalid record limit"
            )

        # Check permissions for ordinary reading.

        if request.action == "crm.read_customers":

            if "crm:read" not in principal.scopes:
                raise AuthorizationDenied(
                    "Missing CRM read permission"
                )

        # Sensitive export requires additional authority.

        if request.action == "crm.export_customers":

            if "crm:export" not in principal.scopes:
                raise AuthorizationDenied(
                    "Missing CRM export permission"
                )

            if "manager" not in principal.roles:
                raise AuthorizationDenied(
                    "Manager approval authority required"
                )

            if not request.approval_reference:
                raise AuthorizationDenied(
                    "Approval reference required"
                )

        # IMPORTANT:
        # The database tenant comes from the
        # authenticated principal.

        trusted_tenant_id = principal.tenant_id

        return TENANT_RECORDS[trusted_tenant_id][
            :request.record_limit
        ]


# -------------------------------------------------
# 6. SECURITY ADMINISTRATION
# -------------------------------------------------

def disable_security_monitoring(
    principal: Principal,
    approval_reference: str | None,
):

    """
    Security monitoring cannot be disabled by
    either operational AI agent.

    A separately authorized platform administrator
    must have the required scope and approval.
    """

    if "security:admin" not in principal.scopes:
        raise AuthorizationDenied(
            "Missing security administration permission"
        )

    if "platform_security_admin" not in principal.roles:
        raise AuthorizationDenied(
            "Platform security administrator required"
        )

    if not approval_reference:
        raise AuthorizationDenied(
            "Administrative approval required"
        )

    return "Security monitoring change authorized."


# -------------------------------------------------
# 7. RUN OUR DEMONSTRATION
# -------------------------------------------------

if __name__ == "__main__":

    crm = CRMService()

    # Simulated malicious tool request.
    # This represents a request that an attacker
    # tries to make the Work Agent produce.

    malicious_request = ToolRequest(
        action="crm.read_customers",
        requested_tenant_id="tenant_B",
        record_limit=5,
    )

    print("\n=== VULNERABLE APPLICATION ===")

    stolen_records = crm.vulnerable_execute(
        malicious_request
    )

    print("Unauthorized records retrieved:")
    print(stolen_records)

    print("\n=== SECURE APPLICATION ===")

    try:

        result = crm.secure_execute(
            malicious_request,
            SUPPORT_USER,
        )

        print(result)

    except AuthorizationDenied as error:

        print(f"BLOCKED: {error}")

    print("\n=== LEGITIMATE CUSTOMER ACCESS ===")

    legitimate_request = ToolRequest(
        action="crm.read_customers",
    )

    result = crm.secure_execute(
        legitimate_request,
        SUPPORT_USER,
    )

    print("Authorized records:")
    print(result)

    print("\n=== WORK AGENT SECURITY BOUNDARY ===")

    try:

        disable_security_monitoring(
            WORK_AGENT,
            approval_reference="maintenance-001",
        )

    except AuthorizationDenied as error:

        print(f"BLOCKED: {error}")

    print("\n=== SECURITY AGENT SECURITY BOUNDARY ===")

    try:

        disable_security_monitoring(
            SECURITY_AGENT,
            approval_reference="maintenance-001",
        )

    except AuthorizationDenied as error:

        print(f"BLOCKED: {error}")
