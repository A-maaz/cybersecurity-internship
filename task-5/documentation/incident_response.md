# Incident Response Plan & Playbook — PhishAware

## 1. Incident Response Framework
PhishAware implements the industry-standard Incident Response Lifecycle outlined in **NIST Special Publication 800-61 Rev. 2** (Computer Security Incident Handling Guide).

```
┌────────────────────────────────────────────────────────┐
│                   1. PREPARATION                       │
│  - Awareness Training   - SOC Playbooks   - Baselines  │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│               2. DETECTION & ANALYSIS                  │
│  - Anomaly Triggers     - User Reports    - Scope Eval │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                    3. CONTAINMENT                      │
│  - Disable Campaign     - Block Sender    - Advisory   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                    4. ERADICATION                      │
│  - Quarantine URLs      - Purge Messages  - Lock Logs  │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                     5. RECOVERY                        │
│  - Verify Baseline Clean - Remedial Training           │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│               6. POST-INCIDENT ACTIVITY                │
│  - Lessons Learned      - Root Cause      - Metrics    │
└────────────────────────────────────────────────────────┘
```

---

## 2. Case Study Walkthrough: Incident INC-001

### 2.1 Incident Identification & Classification
- **Incident Ticket ID:** `INC-001`
- **Title:** Simulated Phishing Campaign - Credential Verification Vector
- **Category:** Social Engineering / Email Phishing (MITRE ATT&CK T1566.002)
- **Severity Rating:** Medium (Elevated interaction rate among non-privileged user cohort)
- **Status:** Resolved
- **Affected Target Cohort:** 10 Synthetic Employee Mailboxes (`test-user-01` to `test-user-10`)

### 2.2 Phase 1: Detection & Analysis
At 09:00:00 UTC, educational campaign *"Security Verification Awareness Test"* was dispatched to 10 synthetic employee mailboxes. 
- **Telemetry Ingestion:**
  - 8 of 10 employees opened the simulated message.
  - Between 09:04:12 and 09:07:50 UTC, 4 employees clicked the simulated verification hyperlink.
  - Concurrently, between 09:05:15 and 09:09:50 UTC, 6 employees flagged the suspicious email using the integrated SOC Phishing Report button.
- **Autonomous Detection Trigger:**
  - At 09:06:30 UTC, the SOC Detection Engine triggered rule `PHISH-SIM-RULE-104` when the link-click interaction counter exceeded the anomaly threshold ($\ge 3$ clicks).
  - Incident ticket `INC-001` was automatically opened and prioritized in the SOC incident queue.
- **Forensic Threat Vector Analysis:**
  - **Sender Profile:** `IT Security <security@techsecure-training.local>` (Domain impersonation).
  - **Lure Concept:** Urgent re-verification demanded within 24 hours under penalty of account suspension.
  - **Destination URL:** `http://techsecure-auth.local/verify-token` (Mock authentication endpoint).

### 2.3 Phase 2: Containment Procedures
Upon ticket assignment, the Incident Response Team executed immediate containment actions:
1. **Disable Campaign:** The campaign status was flipped from `ACTIVE` to `CONTAINED`. All future outbound dispatches were blocked.
2. **Block Simulated Sender:** The sender address `security@techsecure-training.local` was added to simulated mail transport blocklist rules.
3. **Broadcast Advisory Notice:** A safe educational advisory notification was dispatched to all 10 participants warning them of the active simulation drill.
4. **Mark Contained:** At 09:08:45 UTC, the incident commander updated the incident status to **Contained**.

### 2.4 Phase 3: Eradication Procedures
To ensure total eradication across the simulated environment:
1. **Quarantine Simulation Link:** The routing gateway was updated to intercept all traffic directed to the verification link and route it to the **"Simulation Link Neutralized"** quarantine page.
2. **Preserve Evidence Log:** The simulation event stream (consisting of 36 distinct timestamped events) was locked and archived for compliance verification.
3. **Mark Eradicated:** The incident status was advanced to **Eradicated**.

### 2.5 Phase 4: Recovery & Remediation
1. **Verify Baseline Clean:** The SOC diagnostics confirmed that no lingering simulated sessions were active and test mailboxes were returned to baseline.
2. **Assign Remedial Awareness Training:** The 4 test users who clicked the simulation link (`test-user-01`, `test-user-04`, `test-user-07`, `test-user-08`) were automatically designated for the mandatory PhishAware educational module.
3. **Mark Incident Resolved:** At 09:15:00 UTC, the incident commander formally resolved ticket `INC-001`.

---

## 3. Incident Timeline Table

| Time (UTC) | Milestone / Action | Actor | Classification | Status |
| :--- | :--- | :--- | :--- | :--- |
| **09:00:00** | Campaign Dispatched (10 targets) | Simulation Engine | Campaign Started | `SUCCESS` |
| **09:03:10** | First Email Opened (`test-user-01`) | Synthetic User | Email Opened | `LOGGED` |
| **09:04:12** | First Link Clicked (`test-user-01`) | Synthetic User | Link Interaction | `ALERT` |
| **09:05:15** | First User Report Submitted (`test-user-02`) | Synthetic User | Positive Reporting | `SUCCESS` |
| **09:06:30** | Threshold Anomaly: Incident INC-001 Opened | SOC Detection Engine | Incident Detection | `FLAGGED` |
| **09:07:30** | Threat Indicator Analysis Confirmed | Tier 1 SOC Analyst | Incident Analysis | `EXECUTED` |
| **09:08:00** | Campaign Status Flipped to Disabled | SOC Lead | Containment | `EXECUTED` |
| **09:08:20** | Sender Profile Added to Transport Blocklist | Mail Security Admin | Containment | `EXECUTED` |
| **09:08:45** | Campaign Status Updated to Contained | Incident Commander | Containment | `CONTAINED` |
| **09:10:00** | Link Quarantined & Evidence Locked | SOC Analyst | Eradication | `EXECUTED` |
| **09:11:00** | Remedial Training Assigned to Clickers | Training Coordinator | Recovery | `EXECUTED` |
| **09:15:00** | Remediation Audited & Incident INC-001 Resolved | Incident Commander | Incident Resolved | `RESOLVED` |

---

## 4. Key Performance Indicators (KPIs)
- **Time to Detect (TTD):** 2 minutes, 18 seconds (from first link click to automated incident ticket generation).
- **Time to Contain (TTC):** 2 minutes, 15 seconds (from incident opening to campaign containment confirmation).
- **Total Resolution Time (TTR):** 8 minutes, 30 seconds.
- **Reporting Velocity:** 60% of test cohort submitted reports within 5 minutes of campaign launch, demonstrating effective user vigilance.
- **Vulnerability Rate:** 40% of test cohort clicked the simulation link, highlighting specific training targets for Department of Finance and Operations staff.
