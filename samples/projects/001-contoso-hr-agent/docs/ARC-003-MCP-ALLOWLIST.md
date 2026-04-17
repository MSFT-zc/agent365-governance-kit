<!--
Document Control
- Document ID: ARC-003-MCP-ALLOWLIST-v0.1
- Title: MCP Tool Allowlist
- Status: Draft
- Owner: TBD
- Reviewers: TBD
- Approvers: TBD
- Classification: PUBLIC
- Created: 2026-04-17
- Last Updated: 2026-04-17
- Version: 0.1
-->


# MCP Tool Allowlist

## 1. MCP servers
Define the MCP servers the agent is allowed to invoke.

| MCP server | Purpose | Allowed tools | Auth scope |
|---|---|---|---|
| M365 MCP Server (example) | Read HR docs | sharepoint.search, sharepoint.read | https://graph.microsoft.com/.default |

## 2. Guardrails
- Deny list tools:
- Rate limits:
- Data egress restrictions:

## 3. Change control
- How changes to this allowlist are reviewed and approved: