# Remote HMI Access Project — Zone & Conduit Diagram

Worked example for [`architecture-design-review-worked-example.md`](../docs/architecture-design-review-worked-example.md).

```mermaid
flowchart LR
    subgraph L4["Level 4 — Enterprise"]
        USER["OT Engineer\nCorporate Laptop"]
    end

    subgraph L35["Level 3.5 — DMZ"]
        FW["DMZ Firewall\n(existing, reused)"]
        VPN["VPN Gateway\nNo MFA — GAP: ADR-R1"]
        JMP["Jump Host"]
    end

    subgraph L2["Level 2 — Supervisory Control"]
        HMI["Compressor Station Alpha HMI\nNew: Remote HMI Viewer role"]
    end

    USER -->|"New Conduit — SL not yet defined: ADR-R4"| FW
    FW --> VPN
    VPN -->|"No session recording: ADR-R2"| JMP
    JMP -->|"No SIEM log integration: ADR-R3"| HMI

    style VPN fill:#F8CBCB,stroke:#C62828
    style JMP fill:#FCE8B2,stroke:#F9A825
```

**Disposition:** Conditional Approval — four remediation conditions (MFA enforcement, session recording, SIEM integration, formal SL documentation) must close before the next Biennial Cybersecurity Audit cycle. Full detail in the [worked example](../docs/architecture-design-review-worked-example.md).

**Note:** this conduit intentionally terminates at Level 2 (HMI), not Level 1 (PLC) — satisfying the "no direct Level 0/1-to-Level 4 connectivity" requirement even though four other findings remain open.
