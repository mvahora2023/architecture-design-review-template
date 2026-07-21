# architecture-design-review-worked-example.md

# Architecture Design Review — Worked Example

## Keystone Gas & Electric — Remote HMI Access Project

**Prepared By:** Mahmadarsh Vahora (GRC Analyst, Portfolio Project)

---

## Header Section

| Field | Value |
|---|---|
| Project Name | Remote HMI Access Project — Compressor Station Alpha |
| Requestor | OT Engineering Manager |
| Date Submitted | 2026-05-01 |
| Review Date | 2026-05-15 |
| Reviewer(s) | GRC Analyst; IT Security Manager (co-reviewer) |
| Version | 1.0 |
| Disposition | **Conditional Approval** |

**Regulatory Context:** TSA SD Pipeline-2021-02 §3.5, IEC 62443-3-2, NIST SP 800-82 Rev. 3 Chapter 5

---

## Section 1: Project Description and Scope

| Field | Entry |
|---|---|
| Project Purpose | Allow OT engineers to remotely access the Compressor Station Alpha HMI over VPN from the corporate network, to reduce on-site travel for routine monitoring and minor configuration tasks |
| Systems Affected | CS-ALPHA-HMI-01 (AST-003), CS-ALPHA-VPN-GW (AST-013), CS-ALPHA-JMP-01 (AST-012) |
| Zone(s) Impacted (Purdue Level) | Level 4 (Enterprise, as the access origin) through Level 3.5 (DMZ/VPN termination) to Level 2 (HMI) |
| Data Flows Introduced or Modified | New bidirectional remote desktop/HMI session traffic from corporate network endpoints to the Level 2 HMI, terminating through the existing VPN gateway |
| New Remote Access Paths | Yes — this project is, by definition, the introduction of a new remote access path to a previously on-site-only HMI |
| Third-Party Components Involved | None directly; existing VPN gateway vendor platform is reused, not newly introduced |

---

## Section 2: Zone and Conduit Analysis (IEC 62443)

- [x] Are new conduits between zones documented with data flow diagrams? — *Yes, submitted diagram shows corporate network → VPN gateway → jump host → HMI path.*
- [ ] Is each conduit's Security Level (SL) defined and justified against the target SL for the zones it connects? — **Finding: SL target for the new conduit was not explicitly defined in the submission.**
- [x] Are firewalls, DMZs, or data diodes proposed at all new zone boundary crossings? — *Existing DMZ firewall (AST-006) is reused for this path.*
- [x] Does the design avoid direct connectivity between Level 0/1 (field devices) and Level 4 (enterprise)? — *Yes, the path terminates at the HMI (Level 2), not the PLC (Level 1) directly.*
- [ ] Are wireless connections justified and secured (WPA3, certificate-based auth)? — *N/A, no wireless component in this design.*
- [x] Is unidirectional data flow enforced where operationally feasible? — *N/A for this use case, as bidirectional interactive access is the explicit business requirement.*
- [ ] Is the conduit's protocol identified, and is its authentication/encryption posture documented? — **Finding: RDP-over-VPN was specified, but session-level authentication requirements (beyond VPN login) were not documented.**

*(Remaining Section 2 items reviewed and met; full 19-item checklist available on request.)*

---

## Section 3: Access Control Review

- [ ] Is multi-factor authentication (MFA) required for all remote access introduced by this project? — **Finding: The submitted design shows VPN authentication via username/password only. MFA is not currently enforced on the VPN gateway (consistent with RISK-003 in the companion [[ics-ot-risk-assessment-lab]] project).**
- [x] Are least-privilege role definitions documented for all new user/system accounts created by this change? — *Yes, a dedicated "Remote HMI Viewer" role was defined, separate from full engineering configuration access.*
- [x] Is vendor/contractor access time-boxed for any third-party component involved? — *N/A, no third-party access introduced.*
- [ ] Is session recording/logging enabled for any new remote OT access path? — **Finding: Session recording was not included in the current design and is recommended as a condition of approval.**
- [x] Are default/vendor-standard credentials confirmed changed prior to go-live? — *Confirmed by OT Engineering.*

*(Remaining Section 3 items reviewed and met.)*

---

## Section 4: Data Protection and Logging

- [x] Is encryption in transit enforced for all data crossing zone boundaries as part of this change? — *Yes, VPN tunnel provides transport encryption.*
- [ ] Is SIEM integration planned for any new log source introduced by this project? — **Finding: VPN session logs for this new access path are not currently routed to the central SIEM.**

*(Remaining Section 4 items reviewed and met or not applicable.)*

---

## Section 5: Vulnerability and Patch Management

- [x] Has firmware version been reviewed and validated for the HMI involved? — *Yes, HMI patch level confirmed current as of submission.*
- [x] Is a patch cadence defined for the jump host and VPN gateway? — *Yes, existing quarterly cadence applies; no new asset class introduced.*

*(Remaining Section 5 items reviewed and met.)*

---

## Section 6: Regulatory Compliance Mapping

| Requirement | Regulatory Source | Design Element That Addresses It | Status |
|---|---|---|---|
| MFA for remote/privileged access | TSA SD §4.5 | VPN authentication configuration | **Gap** |
| Zone/conduit SL definition | IEC 62443-3-2 | Section 2 analysis | **Gap** |
| Least-privilege account design | NIST SP 800-82 Rev. 3 §6.2 | "Remote HMI Viewer" role definition | Met |
| Session logging for remote OT access | TSA SD §4.3 | Session recording requirement | **Gap** |
| SIEM integration for new log sources | TSA SD §4.3 | VPN log routing | **Gap** |
| Encryption in transit | IEC 62443-3-3 (SR 4.1) | VPN tunnel | Met |
| Patch cadence for existing asset reuse | TSA SD §4.4 | Existing quarterly cadence | Met |
| No direct Level 0/1 enterprise connectivity | NIST SP 800-82 Rev. 3 Ch. 5 | Path terminates at Level 2 (HMI), not Level 1 | Met |
| Documented architecture design review | TSA SD §3.5 | This ADR document | Met |
| PA PUC reliability/safety consideration | PA PUC oversight | OT Engineering safety sign-off obtained | Met |

---

## Section 7: Risk Summary and Disposition

### Residual Risk Table

| Risk ID | Risk Description | Likelihood | Impact | Risk Level | Mitigating Control | Accepted By |
|---|---|---|---|---|---|---|
| ADR-R1 | Remote VPN access without MFA increases credential-compromise exposure to OT HMI | 4 | 4 | High | Condition: MFA enforcement required prior to go-live | Pending — Conditional |
| ADR-R2 | No session recording for remote HMI access limits post-incident forensic visibility | 3 | 3 | Medium | Condition: Session recording required within 30 days of go-live | Pending — Conditional |
| ADR-R3 | VPN session logs not integrated into SIEM delays detection of anomalous remote access | 3 | 3 | Medium | Condition: SIEM integration required within 60 days of go-live | Pending — Conditional |
| ADR-R4 | Conduit Security Level not formally defined, complicating future architecture reviews | 2 | 2 | Low | Condition: SL target documented and added to network architecture diagram | Pending — Conditional |

### Disposition Decision

☐ Approved — No conditions
☒ **Conditional Approval** — Subject to conditions listed below, with follow-up review by 2026-08-15
☐ Rejected

**Conditions:**
1. Multi-factor authentication must be enforced on the VPN gateway for this access path prior to production go-live.
2. Session recording must be enabled for all remote HMI sessions within 30 days of go-live.
3. VPN session logs for this access path must be integrated into the central SIEM within 60 days of go-live.
4. The conduit's Security Level (SL) target must be formally documented and reflected in the current network architecture diagram prior to the next Biennial Cybersecurity Audit cycle.

**Next Review Date:** 2026-08-15
**Follow-Up Tracking Reference:** ADR-2026-014 (tracked in [[compliance-gap-tracker-v2]])
