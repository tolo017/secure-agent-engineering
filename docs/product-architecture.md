# SurfNet Agent — Product Architecture

## 1. Product Overview

SurfNet Agent is a planned two-in-one AI business
automation and security platform developed by
SurfNet Technologies.

Its target market includes companies and MSMEs.

The platform will be offered through a subscription
SaaS model.

## 2. The Two-Agent Architecture

### SurfNet Work Agent

Responsible for approved business workflows.

Planned capabilities:

- Email processing.
- Customer support assistance.
- CRM operations.
- Document processing.
- Knowledge retrieval.
- Business workflow automation.

### SurfNet Security Agent

Responsible for security monitoring and assessment.

Planned capabilities:

- Prompt injection detection and evaluation.
- Suspicious tool-call monitoring.
- Security policy evaluation.
- Agent behavior monitoring.
- Security testing.
- Audit reporting.
- Security alerts and recommendations.

## 3. Shared Platform Services

- Tenant management.
- Authentication and identity.
- Authorization and policy enforcement.
- Integration connectors.
- LLM orchestration.
- Audit logging.
- Monitoring and alerting.
- Subscription and usage management.

## 4. Security Architecture Principles

1. Each customer must be isolated from other tenants.
2. The Work Agent must not grant itself permissions.
3. The Security Agent must not grant itself permissions.
4. Both agents use independent service identities.
5. Sensitive actions require independent authorization.
6. Privileged actions can require human approval.
7. Security events must be auditable.
8. Secrets must not be stored in model prompts.
9. Agent autonomy must be bounded.
10. Tenant access must be enforced server-side.

## 5. Important Architectural Decision

The AI agents may recommend actions and identify risks.

A deterministic policy enforcement layer must independently
decide whether protected actions are permitted.

Neither agent can bypass this layer.

## 6. Product Development Status

Current implementation:

- Initial FastAPI backend.
- Email intake endpoint.
- Input validation.
- Health-check endpoint.

Planned:

- Work Agent.
- Security Agent.
- Authentication and tenant management.
- Policy enforcement.
- MCP integration.
- RAG.
- CRM integrations.
- Privacy controls.
- Audit logging.
- SaaS subscription infrastructure.
