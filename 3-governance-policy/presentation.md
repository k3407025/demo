# Demo 3 — Governance Scan: Policy Applied to Code

## CEO takeaway

**Security asks “can someone break in?” Governance also asks “should we collect and export this data at all, and can we prove approval?”**

## What to show

Open `governance-policy.md` beside `customer_export.py`, then paste this into Continue:

```text
Act as a governance release gate. Compare customer_export.py with governance-policy.md. Do not assume that missing approval evidence exists, and distinguish a code violation from evidence that must be supplied outside the code.

Return a short table with:
- Status: VIOLATION, NEEDS EVIDENCE, or PASS
- Rule ID
- Exact code evidence (file and line), or missing evidence
- Business impact
- Required action

End with one release decision: PASS or BLOCK. Do not edit files. Use plain language and keep the full answer under 180 words.
```

## Talk track (about 3 minutes)

1. “The business purpose is only to send an email to consenting customers.”
2. “The code also exports identity, birth date, phone, and bank information to a normal CSV.”
3. “The agent compares the code with a human-approved policy profile and links findings to S17 and G3.”
4. “Notice the discipline: it calls visible code a violation, but calls an unseen privacy assessment ‘needs evidence’. It does not invent compliance.”
5. “Management receives an auditable release decision and exact remediation.”

## Close

> “Governance becomes an early, repeatable release check instead of a late paperwork exercise.”
