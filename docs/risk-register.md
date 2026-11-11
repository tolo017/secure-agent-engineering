# Sentinel Agent — AI Security Risk Register

## 1. Project Context

Sentinel Agent is a simulated enterprise AI assistant.

Its planned capabilities include:

- Reading customer emails.
- Retrieving company documents.
- Interacting with a CRM.
- Preparing and performing authorized CRM updates.

This register assesses the planned target architecture.

The current application skeleton does not yet contain
an LLM, CRM connection or RAG pipeline.

## 2. Risk Scoring Method

Risk Score = Likelihood x Impact

Likelihood:
1 = Rare
2 = Unlikely
3 = Possible
4 = Likely
5 = Almost certain

Impact:
1 = Negligible
2 = Minor
3 = Moderate
4 = Major
5 = Severe

Project risk bands:
1-4   = Low
5-9   = Medium
10-19 = High
20-25 = Critical

Scores are preliminary engineering estimates.
They must be revised after implementation and testing.

## 3. Risk Register

| ID | OWASP Category | Likelihood | Impact | Score | Priority |
|---|---|---:|---:|---:|---|
| R01 | Prompt Injection | 4 | 5 | 20 | Critical |
| R02 | Sensitive Information Disclosure | 4 | 5 | 20 | Critical |
| R03 | Excessive Agency | 4 | 5 | 20 | Critical |
| R04 | Supply Chain | 3 | 4 | 12 | High |
| R05 | Data and Model Poisoning | 3 | 4 | 12 | High |
| R06 | Unbounded Consumption | 3 | 3 | 9 | Medium |
| R07 | Misinformation | 3 | 4 | 12 | High |
| R08 | Hidden Context Exposure | 3 | 3 | 9 | Medium |
| R09 | Vector and Embedding Weaknesses | 3 | 4 | 12 | High |
| R10 | Improper Output Handling | 3 | 5 | 15 | High |

## 4. Risk Details

### R01 - Prompt Injection

Threat:
Malicious instructions enter through customer emails,
attachments or retrieved documents.

Asset:
Agent context and CRM tools.

Impact:
Unauthorized tool requests and information exposure.

Controls:
Untrusted input classification, provenance tracking,
independent authorization and adversarial testing.

### R02 - Sensitive Information Disclosure

Threat:
Unauthorized disclosure of customer information.

Asset:
CRM records, customer data and application logs.

Impact:
Privacy breach and regulatory exposure.

Controls:
Data minimization, access control, PII masking
and protected logging.

### R03 - Excessive Agency

Threat:
The agent has excessive functionality, permissions
or autonomy.

Asset:
CRM tools and delegated credentials.

Impact:
Unauthorized data access or destructive actions.

Controls:
Least privilege, narrow tools, scoped credentials
and human approval.

### R04 - Supply Chain

Threat:
Compromised third-party packages, models or tools.

Asset:
Application dependencies and AI artifacts.

Impact:
Software compromise and data exposure.

Controls:
Dependency pinning, supplier verification,
integrity checks and vulnerability scanning.

### R05 - Data and Model Poisoning

Threat:
Manipulated documents or data enter trusted
knowledge and model pipelines.

Asset:
RAG corpus and model artifacts.

Impact:
Manipulated answers and compromised decisions.

Controls:
Source verification, ingestion permissions,
document integrity and provenance.

### R06 - Unbounded Consumption

Threat:
Excessive prompts, repeated calls or agent loops.

Asset:
Inference resources and API budget.

Impact:
Financial loss and service disruption.

Controls:
Rate limits, token limits, timeouts,
quotas and iteration budgets.

### R07 - Misinformation

Threat:
The model generates unsupported or incorrect
company information.

Asset:
Company policy and customer decisions.

Impact:
Incorrect advice and reputational damage.

Controls:
Verified retrieval, citation checks,
evaluation and human oversight.

### R08 - Hidden Context Exposure

Threat:
Attempts to reveal internal instructions,
tool schemas or operational context.

Asset:
Developer instructions and application configuration.

Impact:
Information that may assist further attacks.

Controls:
External secret management, minimal context,
access controls and monitoring.

### R09 - Vector and Embedding Weaknesses

Threat:
Unauthorized or incorrect retrieval through
weak vector database isolation or filtering.

Asset:
Embeddings, vector indexes and document metadata.

Impact:
Cross-tenant data disclosure.

Controls:
Tenant filters, document authorization,
metadata validation and retrieval testing.

### R10 - Improper Output Handling

Threat:
Unvalidated model output reaches downstream
systems or executable contexts.

Asset:
Backend services and frontend application.

Impact:
Injection, unsafe rendering or unauthorized actions.

Controls:
Schema validation, output encoding,
parameterized queries and tool restrictions.

## 5. Review Requirements

All controls must be tested.

Risk scores must be updated after:

- Security testing.
- Architecture changes.
- New tool integrations.
- New model integrations.
- Security incidents.

## 6. Current Status

Status: Initial risk assessment.

Next activity:
Apply STRIDE threat modeling and map each risk
to the Sentinel Agent data flow.
