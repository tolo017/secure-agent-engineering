# SurfNet Agent - Day 4 Security Lab Report

## Objective

Demonstrate and remediate a confused-deputy
authorization weakness in a simulated CRM integration.

## Environment

- Operating System: Zorin OS
- Python: 3.12
- Application: SurfNet Agent
- Database: Synthetic Python dictionary
- Testing: Python unittest

## Vulnerability Reproduced

The deliberately vulnerable CRM executor trusted
a tenant ID supplied through a tool request.

It used broad service authority without verifying
the requesting principal's tenant permissions.

## Attack Result

The simulated tenant_A user requested tenant_B
customer records.

The vulnerable implementation returned the records.

## Remediation

The secure implementation:

1. Uses an authenticated principal.
2. Rejects agent-controlled tenant overrides.
3. Checks authorization scopes.
4. Checks user roles.
5. Requires approval for sensitive exports.
6. Restricts Work Agent and Security Agent permissions.

## Automated Testing

Ten test cases cover:

- Cross-tenant access.
- Authorized customer reads.
- Unauthorized exports.
- Approval enforcement.
- Work Agent privilege restrictions.
- Security Agent privilege restrictions.
- Administrative approval.

## Limitations

The laboratory simulates the model-generated tool
request. It does not yet test real LLM prompt-injection
behavior or production database authorization.

## Conclusion

The experiment demonstrates why AI-generated
tool requests must not automatically inherit
privileged backend authority.
