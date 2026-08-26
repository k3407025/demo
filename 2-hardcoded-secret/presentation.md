# Demo 2 — Security Scan: A Secret Committed in Source Code

## CEO takeaway

**A key placed in source code can escape through every clone, backup, log, or vendor hand-off. The agent identifies it and gives the incident response, not just a warning.**

Before presenting, state clearly: **the key is fake and cannot access a service.**

## What to show

Open `payment_gateway.py`, then paste this into Continue:

```text
Perform a security scan of this folder before release. Treat all credentials as if they were real, but do not print the full credential in your response. Run the test if terminal access is available.

Report only:
1. Release decision: PASS or BLOCK
2. Severity and finding, with file and line
3. Business risk in plain language
4. Immediate containment actions
5. Permanent fix

Do not edit files. Keep the answer under 140 words for an executive audience.
```

If needed, run:

```bash
python3 -m unittest -v
```

## Talk track (about 2 minutes)

1. “A developer took a shortcut and put an access key directly in the program.”
2. “The agent detects it and masks the value in its report.”
3. “Deleting the visible line is not enough, because source history and copies may retain it.”
4. “The correct response is to block release, revoke and rotate the key, inspect usage, clean history where required, and use the approved secrets service.”

## Close

> “The scan reduces both breach risk and the cost of finding the problem after release.”
