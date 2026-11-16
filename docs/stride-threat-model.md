# SurfNet Agent — STRIDE Threat Model

Version: 0.1
Framework: STRIDE
Status: Preliminary design assessment
Company: SurfNet Technologies

## 1. Scope

This threat model covers the planned SurfNet Agent SaaS
platform, including:

- SurfNet Work Agent.
- SurfNet Security Agent.
- API Gateway.
- Identity and Tenant Management.
- Policy Enforcement Layer.
- MCP and business integrations.
- RAG and Vector Database.
- PostgreSQL.
- Audit and Security Event Storage.

## 2. Security Objectives

Confidentiality:
Prevent unauthorized access to customer information.

Integrity:
Prevent unauthorized changes to business data and policies.

Availability:
Maintain reliable service despite abusive workloads.

Authentication:
Verify users, services, agents and integrations.

Authorization:
Restrict actions according to identity, tenant,
role and scope.

Accountability:
Maintain reliable evidence of agent and user actions.

## 3. STRIDE Threat Register

| ID | Category | Threat | Proposed Mitigation | Validation |
|---|---|---|---|---|
| SF-S01 | Spoofing | Company A user forges Company B tenant identity | Server-side identity and tenant resolution | Test cross-tenant identity substitution |
| SF-S02 | Spoofing | Forged CRM webhook or connector identity | Verify signatures and authenticated service identity | Submit invalid signature |
| SF-T01 | Tampering | Malicious modification of emails or policy documents | Provenance, integrity checks and restricted ingestion | Modify a test document |
| SF-T02 | Tampering | Customer ID or tool parameters manipulated | Strict schema validation and resource authorization | Replace authorized customer ID |
| SF-T03 | Tampering | Security rules or audit records altered | Restricted policy changes and protected append-only logs | Attempt unauthorized alteration |
| SF-R01 | Repudiation | User denies approving a CRM change | Record identity, timestamp and approval evidence | Reconstruct a test transaction |
| SF-I01 | Information Disclosure | Company A retrieves Company B documents | Tenant isolation, RLS and vector access filters | Test unauthorized retrieval |
| SF-I02 | Information Disclosure | PII or API secrets leak into model requests or logs | Data minimization, masking and secrets management | Test with synthetic sensitive data |
| SF-D01 | Denial of Service | Excessive API requests or oversized attachments | Rate limits, size limits and quotas | Test controlled request bursts |
| SF-D02 | Denial of Service | Agent enters excessive loops or tool calls | Execution budgets, timeouts and circuit breakers | Test a bounded loop |
| SF-E01 | Elevation of Privilege | Prompt injection causes an administrative tool request | Independent authorization and least privilege | Submit a malicious email test |
| SF-E02 | Elevation of Privilege | Work Agent attempts Security Agent administrative actions | Separate identities and permission scopes | Attempt cross-agent privilege access |
| SF-E03 | Elevation of Privilege | User manipulates role or permission claims | Server-side role validation and RBAC | Submit forged role claims |

## 4. SaaS Isolation Requirements

Each tenant must have independently enforced:

- Authentication context.
- Authorization decisions.
- Database access.
- Vector retrieval access.
- Integration credentials.
- Audit access.
- Usage quotas.

Client-supplied tenant IDs must never be the sole
basis for determining resource ownership.

## 5. Security Architecture Decisions

1. Both agents use separate service identities.
2. Work Agent tool requests pass through policy enforcement.
3. Security Agent findings do not automatically grant permissions.
4. Sensitive actions require explicit authorization.
5. Administrative actions have separate approval requirements.
6. Audit events are protected from unauthorized modification.
7. Tenant context is enforced at the data-access layer.

## 6. Risk Scoring

Risk Score = Likelihood x Impact

Likelihood and impact range from 1 to 5.

The scoring is preliminary and must be recalculated
after implementation and testing.

## 7. Assumptions and Limitations

This document describes a planned SaaS architecture.

The current application does not yet implement the
Work Agent, Security Agent, CRM integrations, RAG,
authentication or production tenant isolation.

Proposed mitigations must be verified through
implementation and security testing.

## 8. Next Activities

- Refine trust boundaries.
- Develop detailed attack trees.
- Examine confused deputy scenarios.
- Build authentication and authorization controls.
- Create security regression tests.
