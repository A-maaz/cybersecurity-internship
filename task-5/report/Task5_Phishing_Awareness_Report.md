# Task 5 Capstone Project Final Report
# PhishAware — Phishing Awareness Simulation & Incident Response Platform

**Author:** Cybersecurity Engineering Intern  
**Project Track:** Cybersecurity Capstone Internship (Task 5)  
**Date:** September 2026  
**Classification:** Controlled Educational Cybersecurity Exercise  
**Environment:** Localhost Sandbox / Python 3.13 / Flask / SQLite  

---

## Executive Summary
This report documents the design, implementation, and operational outcomes of the **PhishAware** platform—a controlled educational phishing-awareness and incident-response environment created for the Cybersecurity Internship Task 5 Capstone. 

Phishing and credential-harvesting attacks remain the predominant initial access vector exploited by modern adversaries (MITRE ATT&CK T1566). Technical controls such as secure email gateways and endpoint detection agents must be complemented by behavioral human defense and rapid SOC incident response. 

PhishAware models the complete 12-stage cybersecurity lifecycle in a strictly safe, ethical sandbox that guarantees **zero password collection or credential harvesting**. Operating on synthetic employee fixtures, the platform demonstrates realistic simulation dispatch, real-time telemetry logging, automated anomaly detection, containment, eradication, recovery, and post-incident analysis. During the baseline demonstration campaign (*"Security Verification Awareness Test"*), 10 synthetic targets were evaluated, achieving an 80% open rate, a 40% click rate, and a 60% reporting rate. Incident `INC-001` was detected within 2 minutes 18 seconds and successfully contained in 2 minutes 15 seconds.

---

## 1. Introduction
Social engineering circumvents perimeter fortifications by targeting human trust, urgency, and cognitive bias. The goal of this capstone project is to provide a complete, demonstrable web application that bridges security awareness training with hands-on SOC incident triage.

---

## 2. Project Objectives
1. Build a modular full-stack web application adhering to ethical safety guidelines.
2. Model realistic phishing attack indicators without collecting real credentials.
3. Stream timestamped interaction telemetry to an embedded SQLite store.
4. Provide a real-time SOC Operations Dashboard featuring dynamic Chart.js metrics.
5. Demonstrate a 6-stage NIST SP 800-61 incident response lifecycle.
6. Provide actionable educational awareness curricula and interactive quizzes.

---

## 3. Scope
The project scope is strictly bounded to an educational localhost environment:
- **Target Audience:** Synthetic employee profiles across Corporate, Finance, HR, Operations, Engineering, Sales, and Legal divisions.
- **Allowed Operations:** Local webmail simulation, simulated link-click logging, browser warning redirects, SOC dashboard telemetry, simulated firewall/transport blocks.
- **Strictly Prohibited:** Password fields, authentication capture, credential replay, external email routing, and real-world domain targeting.

---

## 4. Threat Scenario
- **Threat Actor Persona:** Sophisticated external social engineering group targeting corporate identity infrastructure.
- **TTP:** MITRE ATT&CK T1566.002 (Spearphishing Link).
- **Lure Concept:** Urgent notice purporting to originate from *"IT Security"* alleging unauthorized account access and demanding credential verification within 24 hours to prevent single sign-on (SSO) termination.
- **Sender Profile:** `IT Security <security@techsecure-training.local>` (Spoofed display label).

---

## 5. System Architecture
The application implements a 3-tier modular architecture:
1. **Presentation Tier:** Responsive web interface built with Bootstrap 5, featuring a simulated corporate webmail inbox, educational landing pages, and interactive quiz components.
2. **Application Tier:** Python 3 Flask server orchestrating simulation routing, event logging, and incident response playbooks.
3. **Data Tier:** Embedded SQLite database managed via SQLAlchemy ORM, enforcing strict separation of non-sensitive telemetry.

```text
[ Test User Browser ] <──(HTTP / Webmail)──> [ Flask Web App ] <──(SQLAlchemy)──> [ SQLite Event Store ]
```

---

## 6. Tools & Technologies
- **Programming Language:** Python 3.13
- **Web Framework:** Flask 3.1
- **Database / ORM:** SQLite 3, SQLAlchemy 2.1 (Flask-SQLAlchemy 3.1)
- **Frontend / Styling:** HTML5, CSS3, Bootstrap 5.3, Bootstrap Icons
- **Data Visualization:** Chart.js 4.4
- **Testing & Tooling:** Python `unittest`, Pillow, ReportLab

---

## 7. Methodology
The platform follows a 7-stage operational lifecycle:
1. *Planning & Governance:* Scoping test cohorts and enforcing safety guarantees.
2. *Scenario Design:* Authoring realistic social engineering lures with explicit red flags.
3. *Simulation Execution:* Dispatching messages to local test mailboxes.
4. *Security Monitoring:* Logging sent, opened, clicked, and reported events.
5. *Incident Detection:* Triggering automated alerts when interaction thresholds are reached ($\ge 3$ clicks).
6. *Incident Response:* Executing containment, eradication, and recovery playbooks.
7. *Post-Action Analysis:* Generating forensic audit reports and calculating KPIs.

---

## 8. Phishing Simulation
The simulated webmail interface (*TechSecure Webmail*) presents the participant with an authentic enterprise inbox. 

[SCREENSHOT PLACEHOLDER: Simulated Corporate Webmail & Red-Flag Inspector]
*(See screenshots/phishing_email_mockup.png)*

Key simulation features:
- Display name spoofing (`IT Security`) paired with an external sender address.
- Artificial urgency banner (*"Action Required Within 24 Hours"*).
- Interactive **"Red Flag Inspector"** toggle for educational self-study.
- One-click **"Report Suspicious Email (SOC)"** button.
- Benign verification link navigating safely to `/simulation/phishing-link`.

---

## 9. Event Monitoring & Telemetry
Every interaction generates an immutable timestamped event record:
- `CAMPAIGN_STARTED`
- `EMAIL_SENT`
- `EMAIL_OPENED`
- `LINK_CLICKED`
- `PHISHING_REPORTED`
- `INCIDENT_CREATED`
- `CAMPAIGN_CONTAINED`
- `TRAINING_PAGE_VIEWED`
- `INCIDENT_RESOLVED`

[SCREENSHOT PLACEHOLDER: Real-Time Telemetry Event Log]
*(See screenshots/telemetry_event_log.png)*

---

## 10. Detection & Anomaly Triggers
Detection is driven by rule `PHISH-SIM-RULE-104`. When 3 or more synthetic users click the simulated verification link, the detection engine flags an anomalous interaction spike and automatically creates an incident ticket (`INC-001`).

---

## 11. Incident Response Lifecycle
Incident `INC-001` was managed through the 6-stage NIST SP 800-61 framework:
1. Detection $\rightarrow$ 2. Analysis $\rightarrow$ 3. Containment $\rightarrow$ 4. Eradication $\rightarrow$ 5. Recovery $\rightarrow$ 6. Post-Incident Analysis.

[SCREENSHOT PLACEHOLDER: Incident Response Workbench & Timeline]
*(See screenshots/incident_response_workbench.png)*

---

## 12. Containment Execution
Containment actions executed by the incident team:
- **Campaign State:** Flipped to `CONTAINED`.
- **Mail Filter Blocklist:** Simulated transport rule applied to `@techsecure-training.local`.
- **User Advisory:** Educational broadcast dispatched to all test mailboxes.
- **Containment Timestamp:** 09:08:45 UTC.

---

## 13. Eradication Execution
- **URL Quarantine:** Verification link gateway updated to display a *"Threat Neutralized"* block notice.
- **Evidence Preservation:** Event log hashes preserved for forensic audit.
- **Eradication Timestamp:** 09:10:00 UTC.

---

## 14. Recovery Execution
- **Baseline Verification:** Clean test environment confirmed.
- **Remedial Education:** Mandatory interactive phishing curriculum assigned to clicking users.
- **Ticket Resolution:** Incident formally marked `RESOLVED` at 09:15:00 UTC.

---

## 15. Findings & Risk Analysis
- **Overall Open Rate:** 80% (8/10 opened).
- **Vulnerability (Click) Rate:** 40% (4/10 clicked).
- **Vigilance (Report) Rate:** 60% (6/10 reported).
- **Departmental Hotspots:** Finance (100% click rate) and Operations (100% click rate) demonstrated the highest vulnerability to urgency-based lures. Legal, HR, and Sales demonstrated high reporting vigilance.

---

## 16. Mitigation Strategies
1. **Multi-Factor Authentication (MFA):** Enforce FIDO2 / WebAuthn hardware keys to render stolen credentials useless.
2. **Domain Authentication:** Deploy strict DMARC (`p=reject`), DKIM, and SPF policies.
3. **Inbound Email Tagging:** Automatically inject `[EXTERNAL SENDER]` warning banners.
4. **One-Click Reporting:** Provide ubiquitous client reporting add-ins.
5. **Continuous Simulation:** Conduct randomized monthly exercises.

---

## 17. Simulation Results Summary Table

| Metric | Measured Value | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Emails Dispatched** | 10 | 10 | Complete |
| **Open Rate** | 80.0% | < 85.0% | Normal |
| **Click Rate** | 40.0% | < 15.0% | Elevated Risk |
| **Report Rate** | 60.0% | > 50.0% | Strong Vigilance |
| **Training Completion** | 100.0% (Clickers) | 100.0% | Complete |
| **Time to Detect (TTD)** | 2m 18s | < 5m 00s | Optimal |
| **Time to Contain (TTC)**| 2m 15s | < 10m 00s | Optimal |

---

## 18. Lessons Learned
- Proactive employee reporting is the single fastest trigger for incident containment.
- Users consistently prioritize friendly display names over actual sender domains.
- Coercive urgency deadlines induce panic that overrides rational security verification.

---

## 19. Limitations
- Simulation was conducted within a synthetic localhost sandbox; real user cohorts may exhibit varied behavioral nuances.
- Mail transport blocks and firewall quarantines were simulated internally within application state rather than live on enterprise boundary appliances.

---

## 20. Future Improvements
- Multi-vector simulation expansion (Smishing, QR-code Quishing, and USB drops).
- Active Directory / LDAP synchronization for enterprise directory integration.
- Direct SIEM syslog forwarding (CEF/LEEF) to Splunk and Microsoft Sentinel.

---

## 21. Conclusion
The PhishAware platform successfully demonstrates the entire lifecycle of a controlled phishing-awareness simulation and incident response exercise. By pairing realistic social engineering scenarios with rigorous containment playbooks and educational feedback, the platform equips organizations to strengthen their human and operational defenses against modern cyber attacks.

---

## Appendix: Screenshot Placeholders
- `[SCREENSHOT 1: Simulated Phishing Email with Red Flag Toggle]`
- `[SCREENSHOT 2: Safe Awareness Landing Page]`
- `[SCREENSHOT 3: SOC Operations Dashboard with Funnel Charts]`
- `[SCREENSHOT 4: Incident Response Workbench and Forensic Timeline]`
- `[SCREENSHOT 5: Formal Executive Incident Report]`
