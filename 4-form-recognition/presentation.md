# Demo 4 — Form Recognition: Detecting a Logical Error

## Management takeaway

**AI can compare information across pages and apply a supplied business rule to flag inconsistent form completion before processing.**

## What to show

Upload `demo_pdf/abc_limited_wrong_filled_local_bank.pdf` to an AI tool that can read PDF pages visually, then paste this prompt:

```text
Review @/4-form-recognition/demo_pdf/abc_limited_wrong_filled_local_bank.pdf the  annuity application against this business rule:
When Local Bank Account is selected, the customer signature and date in the declaration for Chinese Mainland Bank Accounts must remain blank.

Inspect the actual checkbox marks and signature fields. Do not treat a printed signature label as a signature, or an option label as a selected checkbox.

Return a short table with:
- Bank account selection and page number
- Whether a customer signature or date is present in the Chinese Mainland declaration, and page number
- Business rule result
- Required action

End with one result: PASS, REVIEW REQUIRED, or MANUAL REVIEW REQUIRED if the evidence is unclear. PASS applies only to this rule, not the whole application. Do not infer the cause of an error or authenticate the signature. Do not edit the form. Use plain language and keep the answer under 150 words.
```

Show page 1 and page 3 beside the result so the evidence can be checked immediately. All customer and bank details in this demo are fictional.

## Expected result

| Evidence | Finding |
| --- | --- |
| Page 1 — Bank account selection | Local Bank Account selected; Chinese Mainland Bank Account not selected |
| Page 3 — Chinese Mainland declaration (continued) | Customer signature “Chan Tai Man” and date “07/09/2026” present |
| Business rule result | REVIEW REQUIRED — signature and date in an inapplicable declaration |
| Required action | Review and correct the signature placement and date before processing |

The form demonstrates an inconsistency. The document alone does not establish that a programming defect caused it.

## Talk track (about 3 minutes)

1. “This customer selected a local bank account on page 1.”
2. “Their signature appears on page 3 in a declaration that applies to Chinese Mainland bank accounts.”
3. “We supply a clear business rule: this declaration must remain unsigned and undated when a local bank account is selected.”
4. “The AI connects the evidence across pages, flags the contradiction, and identifies what needs correction.”
5. “The reviewer can verify both findings directly in the form. If the evidence is unclear, the AI requests manual review.”

## Close

> “AI helps catch inconsistent form completion early, with visible evidence and a clear action for review.”
