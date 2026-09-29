# 12-Minute Capstone Video Presentation Outline — PhishAware

## Presentation Overview
- **Project Title:** PhishAware — Phishing Awareness Simulation & Incident Response Platform
- **Capstone Deliverable:** Internship Task 5 Capstone Demonstration Video
- **Total Duration:** Exactly 12 Minutes (0:00 – 12:00)
- **Presenter:** Cybersecurity Engineering Intern
- **Target Audience:** Academic Evaluators, Internship Supervisors, SOC Leads

---

## Detailed Timestamped Presentation Script & Visual Cues

### [0:00 – 1:00] Segment 1: Introduction & Capstone Problem Statement
- **Visual On-Screen:** PhishAware Homepage (`http://localhost:5000/`), showing the modern dark SOC interface, brand banner, and Authorized Training Environment badge.
- **Talking Points:**
  - Welcome evaluators and introduce yourself as a cybersecurity intern completing Task 5.
  - State the core cybersecurity challenge: Social engineering remains responsible for >80% of corporate data breaches.
  - Introduce **PhishAware**: a full-stack, controlled educational platform designed to simulate realistic phishing attacks, capture safe interaction telemetry, monitor events in real-time, and execute a structured 6-stage incident response lifecycle.
  - **Crucial Safety Statement:** Emphasize upfront that PhishAware strictly operates with synthetic users and local fixtures—it does NOT collect passwords, store credentials, or target real users.

### [1:00 – 2:30] Segment 2: Objectives, Architecture & Threat Model
- **Visual On-Screen:** Switch to `diagrams/architecture.png` (or About page), displaying the 3-tier architecture: Presentation Tier (Test User Browser), Application Tier (Flask Engine & Submodules), and Data Tier (SQLite Event Store).
- **Talking Points:**
  - Walk through the 3 tiers:
    1. *Presentation Tier:* Webmail inbox simulation, safe awareness landing pages, and educational curriculum.
    2. *Application Tier:* Modular Flask architecture comprising the Simulation Engine, Event Logger, SOC Analytics, and Incident Response Playbook handlers.
    3. *Data Tier:* Embedded SQLite relational store containing 5 safe entities (`Campaign`, `TestUser`, `Event`, `Incident`, `IncidentAction`).
  - Highlight the end-to-end 12-step lifecycle: Planning $\rightarrow$ Scenario Creation $\rightarrow$ Simulated Email $\rightarrow$ Interaction $\rightarrow$ Safe Landing $\rightarrow$ Event Logging $\rightarrow$ SOC Monitoring $\rightarrow$ Incident Detection $\rightarrow$ Containment $\rightarrow$ Eradication $\rightarrow$ Recovery $\rightarrow$ Post-Incident Analysis.

### [2:30 – 5:00] Segment 3: Live Phishing Simulation Demonstration
- **Visual On-Screen:** 
  1. Navigate to `/simulation/` and configure a campaign: *"Security Verification Awareness Test"*, selecting 10 synthetic test users.
  2. Click **"Launch Simulation"** and show the Campaign Console with 10 synthetic recipients.
  3. Click **"Open Webmail"** for `test-user-01` (Alex Morgan - Finance) to reveal the simulated corporate email client.
- **Talking Points:**
  - Point out realistic social engineering indicators:
    - Impersonation: Display name *"IT Security"* paired with suspicious external sender `security@techsecure-training.local`.
    - Psychological Coercion: *"Action required within 24 hours to prevent account suspension."*
    - Deceptive Call to Action: *"Verify Account Now"* button.
  - Demonstrate the **"Educational Red Flag Inspector"** toggle switch, illustrating how employees are taught to spot spoofed domains, artificial deadlines, and suspicious URLs.
  - Demonstrate the user actions:
    - Click **"Report Suspicious Email (SOC)"** as `test-user-02` to show positive employee reporting behavior.
    - Click **"Verify Account Now"** as `test-user-01` to trigger safe link redirection.

### [5:00 – 6:30] Segment 4: Safe Phishing Landing Page & Awareness Training
- **Visual On-Screen:**
  1. The user lands on `/simulation/phishing-link` showing the **"Phishing Simulation Detected"** warning page.
  2. Click **"Continue to Security Awareness Training"** to load `/awareness/`.
- **Talking Points:**
  - Highlight the immediate positive reinforcement on the landing page: *"No password or sensitive information was collected."*
  - Review the 5 warning signs highlighted for the employee.
  - Tour the **Awareness Training Portal**:
    - The Golden Rule: *"If an unexpected message asks you to act urgently, verify it through an independent trusted channel."*
    - The 6-Step Defense Protocol: Stop & Verify, Inspect Sender, Hover Over Links, Never Enter Credentials, Report to SOC, Verify via Known-Good Channels.
  - Demonstrate the **Interactive Threat Spotter Quiz** by answering Scenario 1 and showing the real-time scoring and feedback.

### [6:30 – 8:00] Segment 5: SOC Dashboard & Live Telemetry Monitoring
- **Visual On-Screen:** Navigate to `/dashboard/` showcasing the live SOC Operations Dashboard.
- **Talking Points:**
  - Review the primary KPI metrics:
    - Emails Dispatched: 10
    - Emails Opened: 8 (80% Open Rate)
    - Links Clicked: 4 (40% Click Rate / Vulnerability Score)
    - Reports Submitted: 6 (60% Vigilance Score)
    - Training Completed: 4
  - Explain the 3 Chart.js visualizations:
    - *Interaction Funnel:* Tracking conversion drop-off across sent, opened, clicked, reported, and trained.
    - *Outcome Distribution Donut:* Proactive reporters vs vulnerable clickers.
    - *Department Risk Breakdown:* Identifying Finance as high-risk vs HR/Legal as highly vigilant.
  - Showcase the real-time Telemetry Stream and demonstrate the instant text search filter.
  - Demonstrate the **"Export CSV Audit Log"** button, showing instant download of `phishaware_simulation_events.csv`.

### [8:00 – 10:30] Segment 6: Incident Response Simulation (NIST IR Lifecycle)
- **Visual On-Screen:** Navigate to `/incidents/` and click into Incident `INC-001`.
- **Talking Points:**
  - Walk through the incident lifecycle:
    1. **Detection:** Autonomous trigger `PHISH-SIM-RULE-104` fired due to click volume threshold ($\ge 3$ clicks).
    2. **Analysis:** Correlating affected user cohort and vector characteristics.
    3. **Containment (Live Action Execution):**
       - Click **[Disable Campaign]** to flip simulation state.
       - Click **[Block Simulated Sender]** to simulate transport rule enforcement.
       - Click **[Broadcast Advisory Notice]** to inform participants.
       - Click **[Mark Contained]** to update the incident status.
    4. **Eradication:**
       - Click **[Quarantine Link Gateway]** to show how attempting to click the link now displays the *"Threat Neutralized"* page.
       - Click **[Lock & Hash Evidence]**.
    5. **Recovery:**
       - Click **[Verify Clean Baseline]**.
       - Click **[Assign Remedial Training]**.
       - Click **[Mark Incident Resolved]** to finalize the ticket.
  - Walk through the interactive **Chronological Incident Timeline** showing each recorded milestone.
  - Click **"Generate Formal Report"** (`/incidents/1/report`) to demonstrate the executive audit report ready for printing or PDF archiving.

### [10:30 – 11:30] Segment 7: Strategic Mitigations & Lessons Learned
- **Visual On-Screen:** Switch to `documentation/lessons_learned.md` or the Executive Report Recommendations section.
- **Talking Points:**
  - Summarize the key lessons learned from the simulation:
    - Technical defenses alone are insufficient; user reporting speed was the deciding factor in early detection.
    - Need for visible `[EXTERNAL]` email banners to combat display-name spoofing.
    - Defense-in-depth: Hardware-backed MFA (FIDO2 / WebAuthn) renders credential harvesting attempts harmless.
    - Implementation of strict DMARC (`p=reject`), DKIM, and SPF domain authentication.

### [11:30 – 12:00] Segment 8: Conclusion & Q&A Wrap-Up
- **Visual On-Screen:** Return to the PhishAware homepage.
- **Talking Points:**
  - Summarize the accomplishments of the Task 5 Capstone:
    - 100% safe, educational platform.
    - Complete modeling of social engineering simulation and SOC incident response.
    - Clean, beginner-friendly Python/Flask/SQLite codebase.
    - Verified test suite and comprehensive documentation.
  - Thank the supervisors and evaluators for their mentorship throughout the cybersecurity internship.

---

## Pre-Recording Checklist
- [ ] Virtual environment activated (`venv`).
- [ ] Dependencies installed via `pip install -r requirements.txt`.
- [ ] Application running on `http://127.0.0.1:5000/`.
- [ ] Click **"Re-Seed Demo Fixtures"** or `/demo-seed` before recording to ensure pristine demo metrics.
- [ ] Browser set to 1080p full-screen display with 100% zoom.
- [ ] Microphone audio levels tested and noise suppression enabled.
