# Phishing Awareness Simulation & Incident Response Methodology

## 1. Overview of the 7-Stage Methodology
The **PhishAware** platform is built around a rigorous 7-stage operational cybersecurity methodology. This methodology adheres to industry standards, including **NIST SP 800-61 Rev. 2** (Computer Security Incident Handling Guide) and **ISO/IEC 27035** (Information Security Incident Management), tailored specifically for ethical social engineering awareness exercises.

```
┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│  1. Planning   │ ──> │ 2. Scenario    │ ──> │ 3. Simulation  │
│  & Governance  │     │    Design      │     │    Execution   │
└────────────────┘     └────────────────┘     └────────────────┘
                                                       │
                                                       ▼
┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│ 7. Post-Action │ <── │ 6. Incident    │ <── │ 4. Security    │
│    Analysis    │     │    Response    │     │    Monitoring  │
└────────────────┘     └────────────────┘     └────────────────┘
                               ▲                       │
                               │                       ▼
                               │              ┌────────────────┐
                               └───────────── │  5. Incident   │
                                              │    Detection   │
                                              └────────────────┘
```

---

## 2. Stage-by-Stage Breakdown

### Stage 1: Project Planning & Governance
- **Objective:** Establish the rules of engagement, ethical boundaries, target audience, and risk mitigation protocols before any simulation occurs.
- **Key Actions:**
  - Define test user cohorts (e.g., 10 synthetic employee identities distributed across Finance, HR, Operations, Engineering).
  - Enforce zero credential collection policies: Under no circumstances will login forms, passwords, or session tokens be ingested.
  - Establish authorization boundaries: All operations are confined to private localhost network testing.

### Stage 2: Threat Scenario Design
- **Objective:** Model realistic threat actor tactics, techniques, and procedures (TTPs) based on observed cyber threat intelligence (MITRE ATT&CK T1566: Phishing).
- **Core Scenarios Modeled:**
  - *Account Verification Phishing:* Spoofed internal IT identity demanding re-verification within 24 hours under penalty of account suspension.
  - *Urgent Password Reset Notice:* Deceptive single sign-on (SSO) alert exploiting artificial deadlines.
  - *Payroll / Tax Compliance Update:* Human resources vector targeting personal direct deposit information.
  - *Cloud Storage Quota Alert:* Infrastructure impersonation alleging system overflow.
- **Embedded Indicators:** Spoofed sender addresses (`techsecure-training.local`), high-urgency language, generic salutations, and mismatched hyperlink destinations.

### Stage 3: Simulation Execution
- **Objective:** Dispatch the controlled exercise to the designated synthetic employee inboxes without transmitting unsolicited traffic over public networks.
- **Operational Workflow:**
  - When the campaign administrator clicks **"Launch Simulation"**, the application creates recipient user fixtures in `test_users`.
  - An initial `CAMPAIGN_STARTED` event is registered.
  - The simulation engine issues `EMAIL_SENT` events for each participant mailbox.
  - Test mailboxes become available for interactive evaluation in the simulation console.

### Stage 4: Security Telemetry & Monitoring
- **Objective:** Ingest and visualize real-time user interaction events through a centralized SOC monitoring interface.
- **Telemetry Ingestion Pipeline:**
  - `EMAIL_OPENED`: Logged when an employee views the simulated email.
  - `LINK_CLICKED`: Safely logged when an employee clicks the "Verify Account" hyperlink.
  - `PHISHING_REPORTED`: Logged when an employee exercises positive reporting behavior via the webmail report button.
  - `TRAINING_PAGE_VIEWED`: Logged when an employee reviews the educational awareness training curriculum.
- **Analytics Visualization:**
  - **Interaction Funnel:** Sent (100%) $\rightarrow$ Opened $\rightarrow$ Clicked $\rightarrow$ Reported $\rightarrow$ Trained.
  - **Outcome Distribution:** Proactive Reporters vs. Vulnerable Clickers vs. Passive Observers.
  - **Department Risk Profiling:** Department-by-department vulnerability scoring to identify high-risk organizational units.

### Stage 5: Incident Detection & Escalation
- **Objective:** Identify anomalous simulation interaction patterns that indicate an active or widespread social engineering outbreak.
- **Detection Mechanisms:**
  - *Automated Threshold Trigger:* If $\ge 3$ users click the simulated malicious link within a campaign window, detection rule `PHISH-SIM-RULE-104` triggers automatic incident ticket generation.
  - *User Report Aggregation:* Multiple user reports dispatched to the SOC within minutes correlate to flag a coordinated phishing barrage.
  - *Manual Escalation:* SOC analysts can escalate any suspicious campaign to the incident response team via the campaign console.

### Stage 6: Incident Response & Mitigation
- **Objective:** Execute containment, eradication, and recovery playbooks to neutralize the simulated threat.
- **Playbook Procedures:**
  - **Containment:** Disable the active campaign, inject mail gateway transport blocks on the sender domain, and broadcast urgent advisory notices to participants.
  - **Eradication:** Neutralize the simulated verification URL (redirecting all traffic to the blocked notice / awareness portal) and lock forensic evidence logs.
  - **Recovery:** Verify environment baseline hygiene and designate mandatory remedial security awareness training for vulnerable staff.

### Stage 7: Post-Incident Analysis & Lessons Learned
- **Objective:** Review campaign outcomes, quantify organizational risk metrics, document forensic timelines, and produce formal executive audit documentation.
- **Deliverables:**
  - Time-to-Detect (TTD) and Time-to-Contain (TTC) calculations.
  - Identification of behavioral root causes (e.g., susceptibility to artificial urgency).
  - Export of timestamped CSV forensic logs (`/export/events.csv`).
  - Formal Executive Incident Response Report generation (`SEC-IR-INC-001`).

---

## 3. Data Flow & Security Model

```text
[Simulated Corporate Webmail] ──(Safe Interaction)──> [Flask Application Gateway]
                                                              │
                     ┌────────────────────────────────────────┴────────────────────────────────────────┐
                     ▼                                                                                 ▼
         [Telemetry Logger]                                                                  [Awareness Engine]
                 │                                                                                     │
                 ▼                                                                                     ▼
    [SQLite: Event / Incident]                                                            [Safe Landing / Quiz]
                 │
                 ▼
       [SOC Dashboard / Reports]
```

1. **Isolation:** The webmail client, simulation engine, and SOC backend operate within a unified, self-contained local Flask sandbox.
2. **Zero Storage of Sensitive Input:** The simulated "Verify Account" CTA uses standard GET requests leading directly to benign educational routes (`/simulation/phishing-link`), completely avoiding `<form>` password input capture.
3. **Audit Immutability:** Event timestamps are recorded in UTC using timezone-aware Python datetimes, ensuring consistent forensic timeline ordering.
