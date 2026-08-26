# Demo 1 — Vendor Update: Find the Regression Before Release

## CEO takeaway

**A small vendor code change could pay the same HK$8,000 refund twice. The agent finds the change, explains the financial impact, and recommends blocking the release.**

## What to show

Open `vendor_v1.py` and `vendor_v2.py` side by side. Point out only that v1 is approved and v2 is the new vendor delivery; do not explain the bug yet.

Paste this into Continue:

```text
Review this vendor upgrade before production. Compare vendor_v1.py (approved 2.0.0) with vendor_v2.py (candidate 2.1.0), and inspect test_vendor_update.py. Run the test if terminal access is available.

Report only:
1. Release decision: PASS or BLOCK
2. The single most important regression, with file and line
3. Business impact in plain language
4. Recommended action for the vendor

Do not edit any file. Keep the answer under 120 words for an executive audience.
```

If needed, run this in the demo folder:

```bash
python3 -m unittest -v
```

## Talk track (about 2 minutes)

1. “This is a routine vendor upgrade, not code written by us.”
2. “The agent compares the approved and candidate versions and runs the acceptance check.”
3. After the result: “The important output is not technical detail. It is a clear release decision, financial impact, and action for the vendor.”
4. “We keep responsibility with management; the agent supplies fast, repeatable evidence.”

## Close

> “The control catches a costly regression before the new version reaches customers.”
