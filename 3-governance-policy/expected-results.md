# Expected Result

## Decision

**BLOCK until the code violations are fixed and review evidence is supplied.**

| Status | Rule | Expected finding | Required action |
|---|---|---|---|
| VIOLATION | GOV-01 | The email campaign exports `full_name`, `hkid`, `date_of_birth`, `mobile`, and `bank_account`, although the declared purpose needs only consent and email. | Remove unnecessary fields from the export. |
| VIOLATION | GOV-02 | HKID and bank-account values are exported directly with no removal or masking. | Do not export them; if a separately approved purpose requires an identifier, minimise and mask it. |
| VIOLATION | GOV-03 | `save_marketing_export` writes personal data to a normal local CSV file. | Use the organisation's approved protected export/transfer service with access control, encryption, retention, and auditability. |
| NEEDS EVIDENCE | GOV-04 | Source code cannot demonstrate a current privacy impact assessment or security risk assessment. | Link approved, current assessment records in the release evidence before production. |

## Business impact

An email list creates a much larger data-loss incident than necessary. A misplaced file could expose identity and financial information, increasing customer harm, regulatory exposure, incident cost, and reputational damage.

## Important interpretation

This demo does not claim that a code agent alone can certify full S17/G3 compliance. It shows two useful outputs:

- deterministic findings where the code is direct evidence; and
- explicit evidence requests where governance depends on approvals, system configuration, or operating process outside the repository.

The department's authorised policy owner and legal/privacy/security functions remain accountable for the real control set and release decision.
