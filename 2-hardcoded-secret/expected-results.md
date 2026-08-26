# Expected Result

## Decision

**BLOCK — High/Critical security finding.**

## Finding

`payment_gateway.py` stores a live-style payment API key in a source constant and sends it in the authorisation header. A good report masks the value, for example `sk_live_DEMO…cdef`, instead of reproducing it.

The demonstration test intentionally fails with:

```text
AssertionError: ... live-style payment key must not be stored in source code
```

## Business impact

Anyone who can read a repository clone, backup, build log, or copied file may obtain the credential and attempt unauthorised payment operations. Removing only the current line does not remove existing copies or history.

## Immediate actions

1. Block the release.
2. Revoke and rotate the exposed credential.
3. Review provider audit logs for misuse.
4. Assess and clean repository history and downstream copies under the incident process.

## Permanent fix

Store the credential in the organisation's approved secrets manager and retrieve it at runtime with least-privilege access, rotation, and audit logging. A local environment variable may illustrate separation in a toy example, but the production control should be the approved managed service.

## Reference

OWASP's [Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) recommends centralised lifecycle management, rotation, least privilege, and secret detection. OWASP's [Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html) says secrets should never be committed to version control.
