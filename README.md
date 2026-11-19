# Secure Agent Engineering

An eight-week practical AI Engineering Security
masterclass and portfolio project.

## Project

SurfNet Agent is a simulated enterprise AI assistant
designed to securely process customer emails, retrieve
company information and interact with a CRM.

## Objectives

- Understand AI application architecture.
- Identify AI attack surfaces.
- Test prompt injection vulnerabilities.
- Secure agent tools and MCP servers.
- Protect RAG knowledge pipelines.
- Implement identity and access controls.
- Protect sensitive information.
- Automate AI security testing.
- Implement audit and governance controls.

## Technology Stack

- Python
- FastAPI
- Pydantic
- PostgreSQL
- Docker
- MCP
- PyRIT
- Garak
- GitHub Actions

## Product Vision — SurfNet Agent

Developed by SurfNet Technologies.

SurfNet Agent is a planned two-in-one AI business
automation and cybersecurity SaaS platform.

### 1. SurfNet Work Agent

Supports authorized business workflows, including:

- Email processing.
- Customer support.
- CRM operations.
- Document processing.
- Business workflow automation.

### 2. SurfNet Security Agent

Provides AI security monitoring and assessment:

- Prompt injection detection.
- Suspicious tool-call monitoring.
- Security policy evaluation.
- Agent behavior monitoring.
- Security testing.
- Audit and compliance reporting.

### Core Security Principle

Both agents operate with distinct identities and
permissions.

A deterministic policy enforcement layer independently
authorizes sensitive operations.

### Target Customers

- Small and medium-sized businesses (SMEs/MSMEs).
- Growing enterprises.
- Organizations adopting AI-powered workflows.

### Business Model

Subscription-based Software as a Service (SaaS).

## 📍 Current Progress

**Program:** AI Engineering Security Masterclass  
**Company Project:** SurfNet Technologies  
**Product:** SurfNet Agent  
**Current Stage:** Stage 1 — AI Attack Surfaces & Threat Modeling  
**Current Status:** Week 1 — Day 4 Completed  
**Weekly Progress:** 4/5 study days completed

### Week 1: AI Attack Surfaces & Threat Modeling

- [x] **Day 1 — AI Security Foundations**
  - Introduction to AI attack surfaces.
  - Understanding threats against LLM-powered applications.
  - Identifying the security responsibilities of AI engineers.

- [x] **Day 2 — Prompt Injection & OWASP LLM Risks**
  - Direct and indirect prompt injection.
  - OWASP Top 10 for LLM Applications.
  - Excessive agency and sensitive information disclosure.
  - Authorization before data retrieval and tool execution.

- [x] **Day 3 — STRIDE Threat Modeling**
  - Applying STRIDE to AI-powered systems.
  - Identifying trust boundaries and security threats.
  - Data-flow analysis.
  - Threat modeling an AI agent interacting with business systems.
  - Designing defensive controls and mitigations.

- [x] **Day 4 — The Confused Deputy Problem**
  - Understanding confused deputy attacks.
  - Tenant isolation and authorization boundaries.
  - Identity-bound authorization.
  - Role-based and scope-based access controls.
  - Least privilege for AI agents.
  - Human approval for sensitive operations.
  - Practical Python implementation of vulnerable and secure authorization patterns.
  - Security testing with Python unit tests.
  - Practical reasoning assessment: 6/6.

- [ ] **Day 5 — Week 1 Consolidation**
  - Consolidate the week's security concepts.
  - Review the SurfNet Agent threat model.
  - Strengthen the practical implementation.
  - Complete the weekly GitHub portfolio milestone.

### Day 4 Practical Deliverables

The confused deputy laboratory includes:

| File | Purpose |
|---|---|
| `labs/day4_confused_deputy.py` | Vulnerable and secure CRM authorization implementations |
| `tests/test_day4_authorization.py` | Authorization and tenant-isolation tests |
| `attacks/confused_deputy/payloads.md` | Synthetic attack payloads for local testing |
| `reports/day4-security-lab.md` | Security findings and defensive recommendations |

### Skills Developed So Far

- AI attack-surface identification.
- Prompt-injection analysis.
- OWASP LLM security fundamentals.
- STRIDE threat modeling.
- Data-flow and trust-boundary analysis.
- Confused deputy vulnerability analysis.
- Multi-tenant authorization.
- Secure AI agent tool access.
- Python security testing.

### Upcoming Milestone

**Week 1 Day 5:** Consolidate the foundations of AI security engineering and prepare the Week 1 portfolio milestone.

---

**Progression Rule:** Complete each practical lesson, test the implementation, document the findings, and push the work to GitHub before moving to the next milestone.

## Security Philosophy

A model-generated decision must never be
treated as automatic authorization.

Security policies and application permissions
must be independently enforced.
