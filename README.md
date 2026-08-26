# CEO Code-Space Demo Kit

Three short demonstrations show how an AI coding agent can act as a release gate inside VS Code.

| Demo | Business question | Intended outcome |
|---|---|---|
| [1 — Vendor update bug](1-vendor-update-bug/presentation.md) | “Could the vendor's new version create a financial loss?” | Block the release and ask the vendor to fix a duplicate-refund regression. |
| [2 — Hardcoded secret](2-hardcoded-secret/presentation.md) | “Could source code expose a key to our systems?” | Block the release, revoke/rotate the key, and move it to an approved secrets manager. |
| [3 — Governance policy](3-governance-policy/presentation.md) | “Does the code follow our data-governance rules?” | Flag excessive personal-data export and request evidence of the required privacy review. |

## Suggested running order

Allow about 3 minutes per demo. For each folder:

1. Open the folder in VS Code.
2. Read its `presentation.md`.
3. Paste the provided prompt into Continue.
4. Compare Continue's answer with `expected-results.md`.

The deliberately insecure values and personal data are fictional. No real secret, customer, or production service is used.

## The single message for the CEO

> The agent converts code into a decision: release, block, or request evidence — with the reason and next action recorded before production.

## Policy basis

- Hong Kong GovCERT describes [S17](https://www.govcert.gov.hk/doc/S17_EN.pdf) as the mandatory baseline and [G3](https://www.govcert.gov.hk/doc/G3_EN.pdf) as its implementation standard.
- G3 v10.2 section 14.6(e) describes source-code review as a way to find bugs, errors, and security flaws, then classify and prioritise repairs.
- S17 section 16.2.3 requires formal testing and review of security measures before implementation.
- S17 section 20.1.4 and G3 section 20.1 cover protection, minimisation, and reduced exposure of personal data.

Detailed source notes are in [research.md](research.md).
