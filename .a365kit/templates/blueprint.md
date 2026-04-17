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

## 1. Agent Summary
- **Agent name:** {{ agent_name }}
- **Purpose:** {{ purpose }}
- **Primary users:** {{ primary_users }}
- **Primary channels/surfaces:** {{ channels }}

## 2. Blueprint scope (design)
> This document describes the intended Agent 365 blueprint configuration before you run `a365 setup`.

### 2.1 Capabilities
List the key capabilities the agent needs.

- Capability 1:
- Capability 2:

### 2.2 Identity & permissions (high level)
- Identity pattern: {{ identity_pattern }}
- Required Microsoft 365 workloads: {{ m365_workloads }}
- Approval model: {{ approval_model }}

## 3. Tooling (MCP)
### 3.1 Allowed MCP servers
Define which MCP servers this agent can call.

- Server: {{ mcp_server_1 }}
  - Tools allowed: {{ mcp_server_1_tools }}

### 3.2 Deny list
- Tools or servers explicitly denied:

## 4. Observability
- Tracing: OpenTelemetry
- Minimum events to log:
  - Agent invocation
  - Tool calls
  - Model inference (if available)

## 5. Security & abuse considerations
- Prompt injection
- Tool abuse
- Data exfiltration

## 6. Next steps
- Run `a365kit identity`, `a365kit mcp-allowlist`, and `a365kit observability`.
- When ready, run `a365kit setup` to call `a365 setup all`.
