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

## Current Progress

### Week 1 - Day 1

- Created initial project structure.
- Built the SurfNet Agent API.
- Implemented email intake validation.
- Classified incoming emails as untrusted.
- Created initial architecture documentation.

## Security Philosophy

A model-generated decision must never be
treated as automatic authorization.

Security policies and application permissions
must be independently enforced.
