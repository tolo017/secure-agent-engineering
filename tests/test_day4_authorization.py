import unittest

from labs.day4_confused_deputy import (
    CRMService,
    ToolRequest,
    AuthorizationDenied,
    SUPPORT_USER,
    WORK_AGENT,
    SECURITY_AGENT,
    PLATFORM_SECURITY_ADMIN,
    disable_security_monitoring,
)


class TestSurfNetAuthorization(unittest.TestCase):

    def setUp(self):
        self.crm = CRMService()

    def test_vulnerable_version_exposes_other_tenant(self):

        request = ToolRequest(
            action="crm.read_customers",
            requested_tenant_id="tenant_B",
        )

        result = self.crm.vulnerable_execute(request)

        self.assertEqual(result[0]["id"], "B201")

    def test_secure_version_blocks_tenant_override(self):

        request = ToolRequest(
            action="crm.read_customers",
            requested_tenant_id="tenant_B",
        )

        with self.assertRaises(AuthorizationDenied):

            self.crm.secure_execute(
                request,
                SUPPORT_USER,
            )

    def test_support_user_can_read_own_tenant(self):

        request = ToolRequest(
            action="crm.read_customers",
        )

        result = self.crm.secure_execute(
            request,
            SUPPORT_USER,
        )

        self.assertEqual(result[0]["id"], "A101")

    def test_support_user_cannot_export_records(self):

        request = ToolRequest(
            action="crm.export_customers",
            approval_reference="approval-001",
        )

        with self.assertRaises(AuthorizationDenied):

            self.crm.secure_execute(
                request,
                SUPPORT_USER,
            )

    def test_manager_needs_approval_to_export(self):

        from labs.day4_confused_deputy import Principal

        manager = Principal(
            user_id="manager_01",
            tenant_id="tenant_A",
            roles=frozenset({"manager"}),
            scopes=frozenset({
                "crm:read",
                "crm:export",
            }),
        )

        request = ToolRequest(
            action="crm.export_customers",
        )

        with self.assertRaises(AuthorizationDenied):

            self.crm.secure_execute(
                request,
                manager,
            )

    def test_manager_can_export_with_approval(self):

        from labs.day4_confused_deputy import Principal

        manager = Principal(
            user_id="manager_01",
            tenant_id="tenant_A",
            roles=frozenset({"manager"}),
            scopes=frozenset({
                "crm:read",
                "crm:export",
            }),
        )

        request = ToolRequest(
            action="crm.export_customers",
            approval_reference="approval-001",
        )

        result = self.crm.secure_execute(
            request,
            manager,
        )

        self.assertEqual(result[0]["id"], "A101")

    def test_work_agent_cannot_disable_security(self):

        with self.assertRaises(AuthorizationDenied):

            disable_security_monitoring(
                WORK_AGENT,
                "approval-001",
            )

    def test_security_agent_cannot_disable_itself(self):

        with self.assertRaises(AuthorizationDenied):

            disable_security_monitoring(
                SECURITY_AGENT,
                "approval-001",
            )

    def test_platform_admin_needs_approval(self):

        with self.assertRaises(AuthorizationDenied):

            disable_security_monitoring(
                PLATFORM_SECURITY_ADMIN,
                None,
            )

    def test_authorized_admin_can_disable_with_approval(self):

        result = disable_security_monitoring(
            PLATFORM_SECURITY_ADMIN,
            "approval-001",
        )

        self.assertIn("authorized", result)


if __name__ == "__main__":

    unittest.main()
