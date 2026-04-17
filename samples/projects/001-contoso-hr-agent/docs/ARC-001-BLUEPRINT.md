<!--
Document Control
- Document ID: ARC-001-BLUEPRINT-v0.1
- Title: Agent 365 Blueprint Design
- Status: Draft
- Owner: TBD
- Reviewers: TBD
- Approvers: TBD
- Classification: PUBLIC
- Created: 2026-04-17
- Last Updated: 2026-04-17
- Version: 0.1
-->


# Agent 365 Blueprint Design

## 1. Agent Summary
- **Agent name:** contoso-hr-agent
- **Purpose:** HR policy Q&A with approvals
- **Primary users:** HR staff
- **Primary channels/surfaces:** Teams

## 2. Blueprint scope (design)
> This document describes the intended Agent 365 blueprint configuration before you run `a365 setup`.

### 2.1 Capabilities
List the key capabilities the agent needs.

- Capability 1:
- Capability 2:

### 2.2 Identity & permissions (high level)
- Identity pattern: Entra-backed Agent Identity (design)
- Required Microsoft 365 workloads: SharePoint
- Approval model: Admin consent workflow

## 3. Tooling (MCP)
### 3.1 Allowed MCP servers
Define which MCP servers this agent can call.

- Server: M365 workload MCP (example)
  - Tools allowed: sharepoint.read

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