# Task 5 — PhishAware

## Phishing Awareness Simulation & Incident Response

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![HTML5](https://img.shields.io/badge/Frontend-HTML5-orange)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Project Overview

**PhishAware** is a controlled cybersecurity awareness platform developed as part of **Task 5 — Capstone Project & Incident Response**.

The project simulates a phishing campaign inside a controlled environment to demonstrate how a security team can:

* Identify phishing indicators
* Monitor user interactions
* Detect a simulated security incident
* Contain the incident
* Simulate eradication and recovery
* Educate users about phishing
* Document the incident response process
* Analyze security-awareness metrics

The application uses **synthetic users and simulated events** and does not collect real passwords or sensitive credentials.

---

## Objectives

The primary objectives of this project are to:

1. Design a controlled phishing-awareness scenario.
2. Develop a web-based phishing simulation platform.
3. Record safe, non-sensitive user interaction events.
4. Visualize simulation metrics through a security dashboard.
5. Simulate phishing incident detection.
6. Demonstrate incident containment and eradication.
7. Document recovery and lessons learned.
8. Provide practical phishing-awareness guidance.
9. Apply secure software-development principles.
10. Produce professional cybersecurity documentation.

---

## Project Workflow

```text
                    PROJECT PLANNING
                           │
                           ▼
                 PHISHING SCENARIO
                     DESIGN
                           │
                           ▼
                 SIMULATED EMAIL
                           │
                           ▼
                   USER INTERACTION
                           │
                           ▼
                 SAFE LANDING PAGE
                           │
                           ▼
                    EVENT LOGGING
                           │
                           ▼
                  SECURITY MONITORING
                           │
                           ▼
                 INCIDENT DETECTION
                           │
                           ▼
                     CONTAINMENT
                           │
                           ▼
                     ERADICATION
                           │
                           ▼
                       RECOVERY
                           │
                           ▼
                  LESSONS LEARNED
```

---

# Features

## Phishing Awareness Simulation

The application presents a realistic but controlled phishing scenario using a fictional organization.

The simulated email demonstrates common social-engineering indicators such as:

* Urgent language
* Suspicious sender information
* Unexpected account verification requests
* Suspicious URLs
* Requests for user action

The simulation does not collect passwords or real credentials.

---

## Safe Phishing Landing Page

When a test user interacts with the simulated phishing link, they are redirected to an educational page.

The page explains:

* That the interaction was part of a controlled simulation
* Which phishing indicators were present
* Why the message was suspicious
* What the user should have done instead

Example:

```text
Phishing Simulation Detected

This was a controlled phishing-awareness exercise.

Warning Signs:

✓ Suspicious sender
✓ Urgent request
✓ Unexpected verification
✓ Suspicious URL
✓ Request for account action

No password or sensitive information was collected.
```

---

# Event Monitoring

The application records only safe simulation events.

Examples include:

```text
CAMPAIGN_STARTED
EMAIL_OPENED
LINK_CLICKED
TRAINING_PAGE_VIEWED
PHISHING_REPORTED
CAMPAIGN_COMPLETED
INCIDENT_CREATED
INCIDENT_CONTAINED
INCIDENT_RESOLVED
```

No passwords, authentication tokens, cookies, or sensitive personal information are stored.

---

# Security Dashboard

The dashboard provides an overview of the simulation.

Example metrics:

| Metric             | Description                                 |
| ------------------ | ------------------------------------------- |
| Emails Simulated   | Number of simulated emails                  |
| Emails Opened      | Number of test users who opened the message |
| Links Clicked      | Number of simulated phishing links clicked  |
| Reports Submitted  | Number of users who reported the message    |
| Incidents Detected | Simulated incidents identified              |
| Incidents Resolved | Incidents successfully closed               |

### Calculated Metrics

**Open Rate**

```text
Opened Emails / Sent Emails × 100
```

**Click Rate**

```text
Clicked Links / Sent Emails × 100
```

**Report Rate**

```text
Reported Emails / Sent Emails × 100
```

All demonstration results are based on **synthetic simulation data**.

---

# Incident Response

The project includes a simulated incident-response workflow based on a phishing event.

```text
Detection
    ↓
Analysis
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Lessons Learned
```

## Detection

The simulated incident can be identified through events such as:

* Suspicious email interaction
* Multiple link clicks
* User phishing report
* Abnormal interaction patterns

---

## Containment

The simulation provides controlled incident-response actions such as:

* Disable simulation campaign
* Block simulated sender
* Notify test users
* Mark incident as contained

These actions modify only the application's simulated state.

---

## Eradication

The simulated response includes:

* Disabling the phishing simulation
* Disabling the simulated malicious link
* Removing the test campaign
* Reviewing affected test users
* Preserving relevant simulation evidence

---

## Recovery

Recovery activities include:

* Verifying the simulation is inactive
* Confirming test accounts are unaffected
* Providing security-awareness training
* Reviewing recommendations
* Documenting lessons learned

---

# System Architecture

```text
                 ┌──────────────────────┐
                 │      Test User       │
                 │      Web Browser     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Flask Web App    │
                 ├──────────────────────┤
                 │ Simulation Engine    │
                 │ Awareness Training   │
                 │ Event Logger         │
                 │ Security Dashboard   │
                 │ Incident Response    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │       SQLite         │
                 │     Event Store      │
                 └──────────────────────┘
```

---

# Technology Stack

### Backend

* Python 3
* Flask
* Flask-SQLAlchemy

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

### Database

* SQLite

### Visualization

* Chart.js

### Development Environment

* Kali Linux
* Windows
* Git
* GitHub

---

# Project Structure

```text
PhishAware/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── database/
│   └── app.db
│
├── models/
│   └── models.py
│
├── routes/
│   ├── main.py
│   ├── simulation.py
│   ├── dashboard.py
│   └── incident_response.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── simulation.html
│   ├── phishing_email.html
│   ├── awareness.html
│   ├── dashboard.html
│   ├── incidents.html
│   └── incident_detail.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── dashboard.js
│   └── images/
│
├── data/
│   └── sample_events.csv
│
├── diagrams/
│   └── architecture.png
│
├── documentation/
│   ├── project_plan.md
│   ├── methodology.md
│   ├── incident_response.md
│   └── lessons_learned.md
│
├── screenshots/
│
├── report/
│   └── Task5_Phishing_Awareness_Report.pdf
│
└── presentation/
    ├── presentation_outline.md
    └── video-link.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/PhishAware.git
cd PhishAware
```

## 2. Create a Virtual Environment

### Linux / Kali Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Initialize the Database

```bash
python init_db.py
```

If database initialization is integrated into the application, simply proceed to the next step.

---

## 5. Run the Application

```bash
python app.py
```

The application should become available at:

```text
http://127.0.0.1:5000
```

---

# Demonstration Workflow

The recommended demonstration workflow is:

### Step 1 — Open PhishAware

Navigate to the homepage.

### Step 2 — Start the Simulation

Launch the predefined phishing-awareness scenario.

### Step 3 — View the Simulated Email

Show the fictional corporate phishing email.

### Step 4 — Interact With the Link

Click the simulated verification link.

No credentials should be requested or collected.

### Step 5 — Analyze the Warning Signs

The awareness page identifies the phishing indicators.

### Step 6 — Open the Dashboard

Review:

* Email interactions
* Link clicks
* Reports
* Event timeline
* Simulation statistics

### Step 7 — Open the Incident

Show the generated simulated phishing incident.

### Step 8 — Perform Incident Response

Demonstrate:

```text
Detection
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
```

### Step 9 — Review Lessons Learned

Show the recommended security-awareness improvements.

---

# Example Simulation Data

The project can use synthetic test users such as:

```text
test-user-01
test-user-02
test-user-03
test-user-04
test-user-05
test-user-06
test-user-07
test-user-08
test-user-09
test-user-10
```

Example demonstration results:

| Simulation Metric  | Example |
| ------------------ | ------: |
| Test Users         |      10 |
| Emails Simulated   |      10 |
| Emails Opened      |       8 |
| Links Clicked      |       4 |
| Reports Submitted  |       6 |
| Incidents Detected |       1 |
| Incidents Resolved |       1 |

> **Note:** These values are synthetic demonstration data and should not be interpreted as real-world user behavior or research findings.

---

# Security Controls

The application follows basic secure-development principles.

Implemented or intended controls include:

* Input validation
* ORM/database parameterization
* CSRF protection for applicable forms
* Secure session configuration
* Environment-based configuration
* No hardcoded secrets
* Safe error handling
* No password collection
* No sensitive information logging

---

# Phishing Awareness Recommendations

The project demonstrates several security-awareness practices.

### Verify the Sender

Check whether the sender address belongs to the expected organization.

### Inspect Links

Hover over links and verify the destination before clicking.

### Avoid Urgency-Based Decisions

Attackers frequently use urgency to encourage users to act without verification.

### Never Share Credentials

Do not provide passwords, MFA codes, or other authentication information through unexpected messages.

### Report Suspicious Messages

Use the organization's established phishing-reporting process.

### Verify Through Another Channel

If a message requests an unusual action, contact the organization using a trusted communication method.

---

# Incident Response Timeline

Example simulated timeline:

```text
09:00 — Simulation Campaign Started
09:03 — Test Email Opened
09:04 — Simulated Link Clicked
09:05 — Phishing Message Reported
09:06 — Incident Detected
09:08 — Campaign Contained
09:10 — Awareness Training Initiated
09:15 — Incident Resolved
```

---

# Findings

The simulation demonstrates how a phishing-awareness exercise can provide visibility into:

* User interaction with suspicious messages
* Common phishing indicators
* Security-reporting behavior
* Incident detection workflows
* Containment procedures
* Security-awareness training requirements

The results are intended for educational demonstration within the controlled test environment.

---

# Mitigation Strategies

Recommended controls include:

1. Regular phishing-awareness training
2. Multi-factor authentication
3. Email filtering
4. Domain and sender verification
5. Phishing-reporting mechanisms
6. Security-awareness simulations
7. User education on suspicious URLs
8. Verification of unusual requests
9. Monitoring of suspicious authentication activity
10. Periodic review of security policies

---

# Screenshots

Screenshots demonstrating the project can be added below.

### Homepage

![Homepage](screenshots/homepage.png)

### Simulated Phishing Email

![Phishing Email](screenshots/phishing-email.png)

### Awareness Page

![Awareness Page](screenshots/awareness-page.png)

### Security Dashboard

![Dashboard](screenshots/dashboard.png)

### Incident Response

![Incident Response](screenshots/incident-response.png)

### Incident Timeline

![Incident Timeline](screenshots/incident-timeline.png)

> Replace the image paths above with the actual screenshots from the project.

---

# Testing Checklist

```text
[✓] Flask application starts successfully
[✓] Homepage loads
[✓] Simulation page loads
[✓] Simulated email displays correctly
[✓] Phishing link redirects safely
[✓] Link-click event is recorded
[✓] Awareness page loads
[✓] Dashboard displays metrics
[✓] Synthetic events are displayed
[✓] Incident can be created
[✓] Incident status can be updated
[✓] Containment action works
[✓] Recovery status can be recorded
[✓] Incident timeline displays correctly
[✓] 404 page works
[✓] Database initializes correctly
```

---

# Limitations

This project is intentionally designed as a controlled educational simulation.

It does not:

* Send real phishing emails
* Collect real credentials
* Target external users
* Interact with real organizational infrastructure
* Perform real account compromise
* Deploy malware
* Conduct unauthorized penetration testing

The metrics are based on synthetic or controlled test data.

---

# Future Improvements

Potential future improvements include:

* Role-based access control
* Multiple phishing scenarios
* Expanded awareness training modules
* More detailed analytics
* Email security-header analysis
* Automated incident reports
* Additional simulation scenarios
* SIEM integration in an isolated environment
* Security-awareness scorecards
* Campaign comparison over time

---

# Internship Task Mapping

This project addresses the required Task 5 components:

| Requirement          | Implementation                                |
| -------------------- | --------------------------------------------- |
| Capstone Selection   | Phishing Awareness Simulation                 |
| Project Planning     | Project objectives, scope, tools and timeline |
| Architecture         | System architecture diagram                   |
| Implementation       | Flask-based simulation platform               |
| Recon / Analysis     | Simulation event analysis                     |
| Evidence             | Screenshots, logs and dashboard               |
| Incident Detection   | Simulated phishing incident                   |
| Containment          | Campaign and link containment                 |
| Eradication          | Removal of simulated threat                   |
| Recovery             | Verification and awareness training           |
| Post-Incident Report | Incident documentation                        |
| Final Documentation  | Professional PDF report                       |
| GitHub Repository    | Source code and methodology                   |
| Presentation         | 12-minute project demonstration               |

---

# Learning Outcomes

Through this project, I gained practical experience with:

* Phishing and social-engineering concepts
* Security-awareness simulation
* Web application development
* Event logging
* Security monitoring
* Incident detection
* Incident-response methodology
* Containment and eradication concepts
* Security documentation
* Secure development practices
* Cybersecurity project presentation

---

# Project Status

**Status:** Completed

**Project Type:** Cybersecurity Capstone

**Environment:** Controlled / Educational

**Focus Areas:**

```text
Phishing Awareness
Web Development
Security Monitoring
Incident Response
Security Documentation
```

---

# Disclaimer

This project was developed strictly for **educational and authorized cybersecurity training purposes**.

The phishing scenarios, users, events, and organizations used in this project are simulated or fictional.

No real credentials or sensitive personal information are collected.

Do not use this project to target real individuals, organizations, or systems without explicit authorization.

---

# Author

**Maaz Abbasi**

Cybersecurity Student | IT & Cybersecurity Enthusiast

GitHub: `YOUR-GITHUB-USERNAME`

LinkedIn: `YOUR-LINKEDIN-PROFILE`

Portfolio: `YOUR-PORTFOLIO-LINK`

---

## Task 5 — Capstone Project

**PhishAware — Phishing Awareness Simulation & Incident Response**

> Building practical cybersecurity skills through controlled security simulations and incident-response exercises.
