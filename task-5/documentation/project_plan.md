# Project Plan — PhishAware Cybersecurity Internship Capstone (Task 5)

## 1. Problem Statement
Social engineering—specifically phishing—remains the leading initial access vector exploited by cyber threat actors worldwide. Over 80% of reported security incidents and enterprise breaches involve human error, credential theft, or deceptive email communications. While perimeter firewalls, email filters, and endpoint detection agents provide vital layers of defense, the human element remains a prime target. Organizations often lack lightweight, safe, and controlled environments to test staff readiness, monitor real-time user behavior, and train incident responders in executing rapid containment and eradication protocols without risking data loss or privacy violations.

## 2. Project Objectives
The objective of the **PhishAware** capstone project is to develop and demonstrate an end-to-end, controlled educational phishing-awareness and incident-response web platform that models the complete operational cybersecurity lifecycle:

1. **Controlled Simulation:** Safe authoring and dispatch of educational phishing scenarios to synthetic test mailboxes.
2. **Safe Telemetry & Zero Harvesting:** Transparent logging of non-sensitive user interactions (`EMAIL_SENT`, `EMAIL_OPENED`, `LINK_CLICKED`, `PHISHING_REPORTED`, `TRAINING_PAGE_VIEWED`) with zero collection or storage of credentials, passwords, or personal data.
3. **Security Operations Monitoring:** Real-time SOC dashboard visualizing interaction funnels, click/report rates, departmental risk distributions, and streaming event logs.
4. **Autonomous Anomaly Detection & Incident Escalation:** Automatic or manual escalation of security incident tickets when interaction thresholds or attack indicators are identified.
5. **Structured Incident Response:** Interactive execution of containment (disabling campaigns, blocking senders, broadcasting advisories), eradication (quarantining URLs, locking evidence), and recovery procedures (verifying baselines, assigning remedial awareness training).
6. **Actionable Education:** Instant educational reinforcement via landing pages, red-flag inspector aids, and interactive threat-spotting quizzes.

## 3. Project Scope
The scope of the project encompasses:
- Full-stack web application developed using Python 3, Flask, SQLAlchemy, SQLite, HTML5, CSS3, Bootstrap 5, and Chart.js.
- Synthetic corporate environment featuring 10 synthetic employee profiles across multiple departments (Finance, HR, Engineering, Operations, Marketing, Sales, Legal, Executive).
- Simulated corporate webmail interface demonstrating realistic phishing lures with spoofed headers, urgency flags, and integrated employee report buttons.
- Real-time telemetry engine recording 10 distinct simulation and incident lifecycle events.
- SOC Operations Dashboard featuring dynamic Chart.js visualizations (Funnel, Outcomes, Departmental Risk) and CSV log export.
- Incident Response Workbench managing the 6-stage NIST SP 800-61 / ISO 27035 lifecycle.
- Professional executive and forensic incident reports formatted for printing and PDF export.

## 4. Out of Scope (Safety Enforcement)
To maintain absolute compliance with legal, ethical, and academic standards:
- **No Real Credential Harvesting:** Password inputs are omitted entirely; no authentication replay or capture is implemented.
- **No Real External Email Transmission:** No emails are transmitted across SMTP to actual external mail servers; all actions occur locally in the test sandbox.
- **No Real Organizational Targeting:** All company names, domains (`@techsecure-training.local`), and test accounts are fictional.
- **No Malware or Exploit Payloads:** Simulation buttons link strictly to benign educational landing pages.
- **No Persistent Agent Deployment:** The application requires no local endpoint agents or system tampering.

## 5. Tools & Technologies
| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Backend Framework** | Python 3.13, Flask 3.1 | Lightweight, reliable, beginner-friendly, rapid prototyping |
| **Data Layer** | SQLite 3, SQLAlchemy 2.1 | Embedded, portable, serverless, parameterized SQL |
| **Frontend Framework** | HTML5, CSS3, Bootstrap 5.3 | Responsive, modern dark SOC aesthetic, zero framework overhead |
| **Visualization** | Chart.js 4.4 | Real-time interactive canvas graphs (Funnels, Donut, Bars) |
| **Icons & Typography** | Bootstrap Icons, Google Inter Font | High-contrast, clean cybersecurity operations design |
| **PDF Generation** | ReportLab 5.0, Pillow 12.3 | Direct automated programmatic PDF generation |
| **Testing** | Python `unittest` | Complete regression test coverage for all routes & triggers |

## 6. Implementation Timeline (Work Breakdown)

```
[Phase 1: Architecture & Planning] ──> [Phase 2: Data Models & Schema]
                 │                                      │
                 ▼                                      ▼
[Phase 3: Core Simulation Engine]   ──> [Phase 4: Simulated Webmail & Landing]
                 │                                      │
                 ▼                                      ▼
[Phase 5: Telemetry & Logging]      ──> [Phase 6: SOC Analytics Dashboard]
                 │                                      │
                 ▼                                      ▼
[Phase 7: Incident Response Module] ──> [Phase 8: Educational Curriculum]
                 │                                      │
                 ▼                                      ▼
[Phase 9: Demo Mode & Test Suite]   ──> [Phase 10: Documentation & Report]
```

- **Phase 1 (Planning & Scoping):** Define system architecture, directory hierarchy, and safety constraints.
- **Phase 2 (Database & Models):** Define `Campaign`, `TestUser`, `Event`, `Incident`, and `IncidentAction` entities.
- **Phase 3 (Simulation Routing):** Implement campaign creation, recipient generation, and simulation state handlers.
- **Phase 4 (Webmail & Landing UI):** Build realistic corporate email interface with red-flag toggles and safe link interceptors.
- **Phase 5 (Telemetry Engine):** Implement safe logging functions with timestamped status tracking and CSV download.
- **Phase 6 (Operations Dashboard):** Build SOC metric cards, Chart.js integrations, and searchable telemetry table.
- **Phase 7 (Incident Response):** Construct 6-stage incident lifecycle workbench with containment/eradication/recovery triggers.
- **Phase 8 (Curriculum & Awareness):** Develop 9 indicators, 6 defense rules, and interactive threat quiz.
- **Phase 9 (Demo Fixtures & Automated Tests):** Write `seed_data.py` and comprehensive `test_app.py` test suite.
- **Phase 10 (Deliverables & Presentation):** Generate architecture diagrams, reports, presentation scripts, and documentation.

## 7. Expected Outcomes & Deliverables
1. Production-ready, runnable local web application operating on `http://127.0.0.1:5000`.
2. Fully populated demo mode allowing instant one-click demonstration for grading and portfolio review.
3. Automated test suite verifying all 11 core functional endpoints with zero errors.
4. Comprehensive GitHub repository with clear instructions for Windows and Kali Linux environments.
5. 12-minute structured demonstration video outline with exact section timestamps.
6. Formal PDF and Markdown capstone reports ready for internship submission.
