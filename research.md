# Research basis for the three CEO demos

Research checked on 25 August 2026. Sources below are primary/official publications. The current public Hong Kong documents found are [S17 v8.2 (April 2025)](https://www.govcert.gov.hk/doc/S17_EN.pdf) and [G3 v10.2 (April 2025)](https://www.govcert.gov.hk/doc/G3_EN.pdf); the [GovCERT resources page](https://www.govcert.gov.hk/en/resources.html) is the official index.

## Read this before claiming “compliance”

- S17 and G3 are HKSAR Government documents for bureaux/departments (B/Ds), and are also intended for vendors, contractors and consultants providing IT services to Government (S17 §§2.1–2.2; G3 §2.2). They are not automatically binding on an unrelated private company. In a company demo, say “mapped to DPO G3/S17” or “company policy based on G3/S17” unless a contract or other requirement makes them applicable.
- S17 defines the mandatory minimum policy requirements. G3 elaborates the requirements and sets implementation standards (S17 §2.3.2). Both documents define **shall** as mandatory, **should** as best practice, and **may** as desirable (S17 §4.2; G3 §4.2). Preserve those words when reporting severity.
- Static scanning can prove that a code pattern exists. It normally cannot prove facts such as whether data really came from production, an exception was approved, or a review occurred. Therefore, findings that depend on context must be labelled “potential non-compliance — confirm”, not stated as a definitive breach.

## Demo 1 — Review a new vendor release and issue an advisory

### Authoritative basis

- [NIST SP 800-218, Secure Software Development Framework v1.1](https://doi.org/10.6028/NIST.SP.800-218), PW.7.1 expressly includes third-party code when deciding when code review/analysis is required. PW.7.2 says discovered issues and recommended remediation should be recorded and triaged; its examples include automated static analysis with human review. PW.8.2 adds scoped testing, documented results, triage, and regression tests for previously reported vulnerabilities.
- G3 §14.6(a) requires a vulnerability-management process covering identification, evaluation, mitigation and tracking. G3 §14.6(e), “Source Code Review” (document page 73; PDF page 83), describes automated or manual review to find bugs, errors and security flaws and to classify and prioritise repairs.
- G3 §16.2(c) (document page 102; PDF page 112) recommends thorough testing and verification for **new and updated applications before production rollout**, proportionate to criticality. G3 §20.2(c) recommends source-code reviews for Internet-facing systems before production and major changes, with issues evaluated and corrected before live-run.
- S17 §17.1.1 requires an external provider serving a B/D to follow departmental and Government security requirements. S17 §17.2.2 requires audit/compliance-monitoring rights or periodic satisfactory security-audit reports. This supports retaining customer oversight rather than accepting “the vendor tested it” as sufficient.

### Recommended tiny showcase

Place `vendor-v1/` and `vendor-v2/` side by side. In v2, change one approval boundary from `amount >= 100000` to `amount > 100000`. Ask the agent to review only the vendor update and prepare a one-page advisory.

Expected finding: an HK$100,000 transaction no longer enters the approval path. The advisory should state the affected version/file/line, business impact, severity, a one-line correction, and a boundary regression test. This is a plain business bug, visually obvious in a diff, and does not overlap the secret or governance demos.

Suggested CEO message: **“A vendor update is not a black box: the code space identifies the changed risk, explains the business impact, and gives management an actionable accept/fix/hold decision before release.”**

## Demo 2 — Detect a plaintext secret in source

### Authoritative basis

- [CISA/FBI Product Security Bad Practices](https://www.cisa.gov/sites/default/files/2025-01/joint-guidance-product-security-bad-practices-508c_0.pdf), item 8, identifies secrets or credentials in source as a dangerous bad practice. It recommends retrieving secrets from a secret manager and integrating credential/secret scanning into development.
- [MITRE CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html) is the precise scanner taxonomy. MITRE describes both inbound hard-coded passwords and outbound credentials used to connect to another service, provides clear-text code/config examples, and recommends keeping credentials outside code in strongly protected storage.
- G3 §11.3(c) requires passwords in storage to be protected with controls such as access control and encryption. G3 §12.1(a) says keys used for encryption/decryption must be kept secret. These support the control objective, but neither sentence alone literally says “all API keys must never appear in source”; CISA item 8 and CWE-798 are the more exact references for this demo.

### Recommended tiny showcase

Use unmistakably fake values, for example `DEMO_DB_PASSWORD = "DemoOnly-NotARealSecret!"` and `DEMO_API_KEY = "demo_live_000000000000"`, in a short configuration module. Never place a real credential in the demo.

Expected finding: file/line, **CWE-798**, high severity, possible unauthorised system/data access, and an advisory to (1) revoke/rotate the exposed value, (2) remove it from code and history, (3) retrieve it from an approved secret manager/environment injection, and (4) scan the repository/history for related exposure. Merely moving the literal to another committed config file is not remediation.

Suggested CEO message: **“The code space catches a digital key before it leaves the building—and recommends containment, not just a cosmetic code change.”**

## Demo 3 — Governance policy-as-code mapped to DPO G3/S17

### Recommended rule: personal/production data in test fixtures

- G3 §16.3(a), “Protection of Test Data” (document page 104; PDF page 114), says test data must be selected and controlled according to classification; production data must not be used for testing; where operational databases with personal/classified information cannot be avoided, review, documentation and Information Owner approval are required; personal data must be de-personalised before use.
- The matching top-level policy is S17 §16.3.1: test data must be selected, protected and controlled in line with its classification. S17 §20.1.2 also requires records evidencing compliance and supporting audits.
- G3 §20.2(b) explains that a security audit evaluates compliance against Government and departmental policies and that non-compliance needs cause analysis, corrective action, effectiveness review, documentation and consideration of similar systems. This is the governance lifecycle the demo should summarise.

Create a test fixture containing **synthetic, clearly labelled demo data** that looks production-like (for example a fictitious name and HKID-shaped value), plus a comment stating that it simulates a production copy. The policy scanner should report:

> Potential personal/production data in test fixture — manual confirmation required. If production-derived, this conflicts with G3 §16.3(a); replace with synthetic/de-personalised data or document the approved exception and controls.

This is the most business-readable example because it links code to customer privacy and audit evidence. The expected result must not claim the fake demo record is a real privacy breach. A pattern match is a governance review trigger; provenance and approval require human evidence.

### Deterministic fallback rule

If a definite code-only pass/fail is preferable, use `hashlib.sha1(...)` for new password hashing. G3 §12.1(a) says password storage should use SHA-2 or equivalent and says SHA-1 **shall not** be used unless it is a legacy system. Report “fail unless the legacy-system exception is documented.” This is easier to prove automatically but is less distinct from conventional security scanning.

Suggested CEO message: **“Security asks whether code is dangerous; governance also asks whether it follows our chosen rules and leaves evidence for audit.”**

## Claims the presenter should avoid

- Do not say an AI/code scanner “certifies S17/G3 compliance.” G3 §20.2 says assessments and audits also require scope, documents, settings, logs, interviews and qualified independent judgement; G3 explicitly says checklists do not substitute for comprehensive assessments.
- Do not treat every tool alert as a confirmed defect. Show the agent’s evidence, confidence, business impact and recommended human decision.
- Do not imply G3/S17 bind all Hong Kong companies. State the actual applicability or explain that the company has adopted the controls as its internal baseline.
- Do not use real credentials or personal data in any demonstration.

## Compact source list

1. HKSAR GovCERT, [Government IT Security Policy and Guidelines resources](https://www.govcert.gov.hk/en/resources.html).
2. Digital Policy Office, [Baseline IT Security Policy S17 v8.2](https://www.govcert.gov.hk/doc/S17_EN.pdf), April 2025.
3. Digital Policy Office, [IT Security Guidelines G3 v10.2](https://www.govcert.gov.hk/doc/G3_EN.pdf), April 2025.
4. NIST, [SP 800-218 SSDF v1.1](https://doi.org/10.6028/NIST.SP.800-218), February 2022.
5. CISA/FBI, [Product Security Bad Practices](https://www.cisa.gov/sites/default/files/2025-01/joint-guidance-product-security-bad-practices-508c_0.pdf), item 8.
6. MITRE, [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html).
