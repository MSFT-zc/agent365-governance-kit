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

## 1. MCP servers
Define the MCP servers the agent is allowed to invoke.

| MCP server | Purpose | Allowed tools | Auth scope |
|---|---|---|---|
| {{ server_1 }} | {{ server_1_purpose }} | {{ server_1_tools }} | {{ server_1_scope }} |

## 2. Guardrails
- Deny list tools:
- Rate limits:
- Data egress restrictions:

## 3. Change control
- How changes to this allowlist are reviewed and approved:
