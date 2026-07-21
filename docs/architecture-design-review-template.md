# architecture-design-review-template.md

# Cybersecurity Architecture Design Review (ADR) Template

**Fictional Utility:** Keystone Gas & Electric
**Prepared By:** Mahmadarsh Vahora
**Purpose:** Reusable review template applied to any proposed OT/IT integration project prior to go-live approval

> **Portfolio Disclosure:** This is a self-directed portfolio artifact. "Keystone Gas & Electric" is fictional.

---

## Header Section

| Field | Value |
|---|---|
| Project Name | [Insert] |
| Requestor | [Insert Name / Department] |
| Date Submitted | [Insert] |
| Review Date | [Insert] |
| Reviewer(s) | [Insert Name(s) / Role(s)] |
| Version | [Insert] |
| Disposition | ☐ Approved ☐ Conditional ☐ Rejected |

**Regulatory Context:** TSA Security Directive Pipeline-2021-02 §3.5 (Cybersecurity Architecture Design Review), IEC 62443-3-2 (Security Risk Assessment for System Design), NIST SP 800-82 Rev. 3 Chapter 5 (Architecture)

---

## Section 1: Project Description and Scope

| Field | Entry |
|---|---|
| Project Purpose | [Describe the business/operational purpose of the proposed change] |
| Systems Affected | [List all systems, by asset ID where applicable] |
| Zone(s) Impacted (Purdue Level) | [Specify Level 0-4 zones touched by this change] |
| Data Flows Introduced or Modified | [Describe new or changed data flows, including direction] |
| New Remote Access Paths | [Describe any new remote access mechanism introduced] |
| Third-Party Components Involved | [List any vendor/third-party hardware, software, or access involved] |

---

## Section 2: Zone and Conduit Analysis (IEC 62443)

- [ ] Are new conduits between zones documented with data flow diagrams?
- [ ] Is each conduit's Security Level (SL) defined and justified against the target SL for the zones it connects?
- [ ] Are firewalls, DMZs, or data diodes proposed at all new zone boundary crossings?
- [ ] Does the design avoid direct connectivity between Level 0/1 (field devices) and Level 4 (enterprise)?
- [ ] If Level 0/1 to Level 4 connectivity cannot be avoided, is a documented, approved exception on file with compensating controls?
- [ ] Are wireless connections (if any) justified and secured using WPA3 or certificate-based authentication?
- [ ] Is unidirectional data flow (e.g., data diode) enforced where operationally feasible, rather than defaulting to bidirectional connectivity?
- [ ] Is the conduit's protocol identified (e.g., Modbus-TCP, DNP3, OPC-UA), and is its authentication/encryption posture documented?
- [ ] Does the design introduce any new trust relationship between previously isolated zones?
- [ ] Are firewall rules for the new conduit scoped to specific ports/protocols/hosts, rather than broad allow-all rules?
- [ ] Is there a rollback plan if the new conduit needs to be disabled post-deployment?
- [ ] Has the OT Engineering team validated that the proposed conduit does not compromise process safety functions?
- [ ] Is the conduit's traffic volume/pattern baseline documented, to support future anomaly detection?
- [ ] Are redundant/failover paths for this conduit identified and reviewed for the same security posture as the primary path?
- [ ] Is the physical network path (cabling, switch ports) for the new conduit documented and access-controlled?
- [ ] Has a threat model been completed specifically for the new conduit (not just the endpoints it connects)?
- [ ] Is there a defined maximum session duration or timeout for any new remote/administrative conduit?
- [ ] Does the change introduce any new internet-facing exposure, directly or indirectly?
- [ ] Are logging and monitoring requirements for the new conduit defined before go-live, not planned as a future enhancement?
- [ ] Has the change been reviewed against the current network architecture diagram to confirm no undocumented conduits are introduced as a side effect?

---

## Section 3: Access Control Review

- [ ] Is multi-factor authentication (MFA) required for all remote access introduced by this project?
- [ ] Are least-privilege role definitions documented for all new user/system accounts created by this change?
- [ ] Is vendor/contractor access time-boxed (not standing/persistent) for any third-party component involved?
- [ ] Is privileged account management (PAM) tooling extended to cover any new privileged accounts introduced?
- [ ] Is session recording/logging enabled for any new remote OT access path?
- [ ] Are default/vendor-standard credentials confirmed changed prior to go-live?
- [ ] Is a periodic access recertification cadence defined for accounts created by this project?
- [ ] Is there a documented emergency access revocation procedure for any new access path?
- [ ] Are shared/generic accounts avoided, or if unavoidable, formally documented with compensating controls?
- [ ] Is the new access path reflected in the organization's current privileged access inventory?
- [ ] Has HR/offboarding process been updated to include any new account types introduced by this project?
- [ ] Is break-glass/emergency access (if applicable) separately logged and alerted on?

---

## Section 4: Data Protection and Logging

- [ ] Is encryption in transit enforced for all data crossing zone boundaries as part of this change?
- [ ] Is historian or process data introduced/modified by this project classified according to the organization's data classification policy?
- [ ] Is SIEM integration planned for any new log source introduced by this project?
- [ ] Does the log retention policy for new log sources align with the organization's minimum retention requirements?
- [ ] Is data at rest encryption applied to any new data store introduced by this change?
- [ ] Are logs from the new component tamper-evident or forwarded to a centralized, access-controlled log destination?
- [ ] Is there a defined data flow map showing where data introduced by this project is stored, transmitted, and ultimately retired?
- [ ] Has a data protection impact assessment been completed if the change involves personal or sensitive operational data?
- [ ] Are backup and recovery procedures defined for any new data store introduced by this project?
- [ ] Is there a documented data disposal/decommissioning procedure for this project's data at end-of-life?

---

## Section 5: Vulnerability and Patch Management

- [ ] Has firmware version been reviewed and validated for all new field devices introduced by this project?
- [ ] Is a patch cadence defined for all new assets prior to go-live (not deferred to a future policy update)?
- [ ] Has a known-CVE check been performed against all new hardware/software components?
- [ ] Is there a documented compensating control for any component that cannot be patched on the standard cadence?
- [ ] Has the vendor provided a security patch support commitment/timeline for the components introduced?
- [ ] Is end-of-life/end-of-support status confirmed as current (not approaching) for all new components?
- [ ] Is vulnerability scanning coverage extended to include any new assets introduced by this project?
- [ ] Has a rollback/patch-testing procedure been defined for OT-specific components introduced by this change?

---

## Section 6: Regulatory Compliance Mapping

| Requirement | Regulatory Source | Design Element That Addresses It | Status |
|---|---|---|---|
| Documented architecture design review prior to OT/IT integration go-live | TSA SD Pipeline-2021-02 §3.5 | This ADR process itself | Met |
| Zone/conduit security level definition | IEC 62443-3-2 | Section 2 Zone and Conduit Analysis | Met |
| No direct Level 0/1-to-Level 4 connectivity without documented exception | NIST SP 800-82 Rev. 3 Ch. 5 | Section 2, item 4-5 | Partial |
| MFA for remote/privileged access | TSA SD §4.5 | Section 3 Access Control Review, item 1 | Met |
| Least-privilege account design | NIST SP 800-82 Rev. 3 §6.2 | Section 3, item 2 | Met |
| Encryption in transit across zone boundaries | IEC 62443-3-3 (SR 4.1) | Section 4, item 1 | Met |
| Log retention and SIEM integration for new sources | TSA SD §4.3 | Section 4, items 3-4 | Partial |
| Patch cadence and CVE review for new assets | TSA SD §4.4 | Section 5, items 2-3 | Met |
| Vendor/third-party access controls | TSA SD §4.8 | Section 3, items 3, 5 | Met |
| PA PUC reliability/safety impact consideration for OT changes | PA PUC oversight requirements | Section 2, item 12 (OT Engineering safety validation) | Met |

---

## Section 7: Risk Summary and Disposition

### Residual Risk Table

| Risk ID | Risk Description | Likelihood | Impact | Risk Level | Mitigating Control | Accepted By |
|---|---|---|---|---|---|---|
| [Insert] | [Insert] | [1-5] | [1-5] | [Low/Med/High/Critical] | [Insert] | [Insert] |

### Disposition Decision

☐ **Approved** — No conditions
☐ **Conditional Approval** — Subject to conditions listed below, with follow-up review by [date]
☐ **Rejected** — Reasons documented below

**Conditions / Rejection Reasons:**
1. [Insert]
2. [Insert]

**Next Review Date:** [Insert]
**Follow-Up Tracking Reference:** [Insert ticket/tracker ID]
