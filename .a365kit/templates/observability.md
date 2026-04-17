<!--
Document Control
- Document ID: {{ document_id }}
- Title: {{ title }}
- Status: Draft
- Owner: {{ owner }}
- Reviewers: {{ reviewers }}
- Approvers: {{ approvers }}
- Classification: PUBLIC
- Created: {{ created_date }}
- Last Updated: {{ updated_date }}
- Version: {{ version }}
-->


# {{ title }}

## 1. Observability goals
- Auditability
- Troubleshooting
- Compliance evidence

## 2. OpenTelemetry requirements
### 2.1 Traces
- Required spans: agent invocation, tool call, model inference

### 2.2 Attributes (minimum)
Define the minimum attributes your org requires (examples):
- tenant_id
- agent_id
- conversation_id

## 3. Retention & access
- Retention period:
- Who can access traces:

## 4. Alerts
- High error rates
- Tool invocation anomalies
