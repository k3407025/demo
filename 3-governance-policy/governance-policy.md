# Demo Governance Profile: Customer Email Campaign

This profile translates selected DPO S17/G3 requirements into reviewable business rules. It is an **illustrative departmental profile**, not an official replacement for S17, G3, legal advice, a privacy impact assessment, or the organisation's complete policies.

## Declared purpose

Send email only to customers who have consented.

## Rules checked in this demo

| Rule | Requirement | Scan outcome |
|---|---|---|
| GOV-01 Data minimisation | Export only `email` and `email_consent`; other personal fields are unnecessary for the declared purpose. | Code rule: fail if other fields are exported. |
| GOV-02 Reduced exposure | Direct identifiers not necessary for the purpose, such as HKID and bank-account data, must be removed; where an identifier is justified, mask or anonymise it where practicable. | Code rule: fail for unmasked HKID or bank account. |
| GOV-03 Protected export | A personal-data export must use the approved protected transfer/storage mechanism, not a normal plaintext CSV file. | Code rule: fail when a plaintext local file is created. |
| GOV-04 Privacy review evidence | Before production or a major change involving personal data, the release record must link to a current privacy impact assessment and security risk assessment. | Evidence rule: `NEEDS EVIDENCE` if source code alone cannot prove it. |

## Source mapping

- **S17 20.1.4:** the Personal Data (Privacy) Ordinance must be observed and all personal data should be classified as RESTRICTED or above.
- **S17 20.2.1:** security risk and privacy impact assessments are required before production rollout and major changes, as well as at least every two years.
- **G3 20.1:** collect and process only the minimum personal data necessary for the identified purpose; minimise exposure through removing or masking identity.
- **G3 12.1(a):** encryption protects confidentiality during transmission and storage.

Official documents: [Baseline IT Security Policy (S17)](https://www.govcert.gov.hk/doc/S17_EN.pdf) and [IT Security Guidelines (G3), version 10.2](https://www.govcert.gov.hk/doc/G3_EN.pdf).
