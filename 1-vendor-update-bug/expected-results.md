# Expected Result

## Decision

**BLOCK candidate release 2.1.0.**

## Finding

`vendor_v2.py` appends every retry message to the refund batch. The approved version tracks `seen_order_ids` and skips a repeated order. The candidate removed that protection.

The acceptance test intentionally fails:

```text
AssertionError: 1 != 2 : one order must be refunded once
```

## Business impact

A retried message can refund one order twice. In the sample, an HK$8,000 refund becomes HK$16,000, creating direct financial loss and reconciliation work.

## Recommended advisory

Ask the vendor to restore idempotency/deduplication by `order_id`, add the retry test to its release suite, and resubmit the version. Do not promote 2.1.0 until the test passes.

## What a good agent answer should not do

- Approve the release because the code runs syntactically.
- bury the release decision in technical detail.
- Edit vendor code without approval; the first action is an advisory and release gate.
