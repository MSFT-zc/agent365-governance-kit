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

## 1. Scope
- Agent: {{ agent_name }}
- Surfaces: {{ channels }}
- Tools: MCP

## 2. Key assets
- Sensitive data types:
- Critical tools/actions:

## 3. Threats (starter list)
- Prompt injection
- Tool misuse / privilege escalation
- Data exfiltration
- Supply chain (tool server compromise)

## 4. Mitigations
- Input/output filtering
- Least privilege tool allowlist
- Human-in-the-loop for sensitive actions
- Monitoring and alerting

## 5. Residual risk
- Document what remains and why.
