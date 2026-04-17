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

## 1. Identity model
- **Agent identity type:** {{ agent_identity_type }}
- **Tenant:** {{ tenant_notes }}

## 2. Permissions & least privilege
### 2.1 Microsoft Graph scopes
List required Graph permissions (least privilege).

- Permission:

### 2.2 Admin consent strategy
- Who grants admin consent:
- How approval/consent is tracked:

## 3. Operational controls
- Key rotation / secrets (if used):
- Break-glass / kill switch:

## 4. Evidence
- Link to blueprint doc: {{ blueprint_doc }}
