# 🔐 Cybersecurity Internship — Task 1

<p align="center">
  <img src="screenshots/banner.png" width="100%">
</p>

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Lab-blue?style=for-the-badge)
![Kali Linux](https://img.shields.io/badge/Kali%20Linux-2026-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![VirtualBox](https://img.shields.io/badge/VirtualBox-Lab-183A61?style=for-the-badge&logo=virtualbox&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---
## Objective

The objective of this task was to build a basic cybersecurity lab using Oracle VirtualBox, Kali Linux, and Metasploitable 2.

The lab provides an isolated environment for learning and practicing cybersecurity concepts safely.

---
### Lab Environment

| Machine | Role | OS |
|---|---|---|
| Kali Linux | Attacker | Kali Linux 2026 |
| Metasploitable 2 | Target | Linux |

---
### Lab Architecture


                Host Computer
                      |
                 VirtualBox
                      |
          ┌───────────┴───────────┐
          │                       │
     Kali Linux             Metasploitable 2
      Attacker                  Target
          │                       │
          └── Private Network ────┘



---

### Setup Steps
1. Install VirtualBox

 - *Installed Oracle VirtualBox on the host machine.*
<p align="center">
  <img src="screenshots/virtualbox.png" width="900">
</p>

2. Download Kali Linux

 - *Downloaded the Kali Linux 2026 ISO for installation as the attacker machine.*
<p align="center">
  <img src="screenshots/kali-iso.png">
</p>

3. Create Kali Linux VM

 - *Created a new Kali Linux virtual machine in VirtualBox and configured:*
<p align="center">
  <img src="screenshots/kali-vm-settings.png" width="900">
</p>

 ```- RAM
  - CPU
  - Virtual storage
  - Network adapter
  - Kali Linux ISO
  ```

4. Install & Configure Kali Linux

 - *Started the VM and completed the Kali Linux installation.*

 - *During installation, I configured:*
<p align="center">
  <img src="screenshots/kali-desktop.png" width="900">
</p>

```
  - Username
  - Password
  - System settings
  - Storage
  - Network
```

5. Download Metasploitable 2

*Downloaded the Metasploitable 2 virtual machine to use as the vulnerable target.*

6. Configure Metasploitable 2

*Imported Metasploitable 2 into VirtualBox and configured its:*

<p align="center">
  <img src="screenshots/metasploitable-settings.png" width="900">
</p>

```
RAM
CPU
Storage
Network adapter
```
7. Configure Lab Network

*Configured both virtual machines to use the same private/host-only network.*
<p align="center">
  <img src="screenshots/metasploitable.png" width="900">
</p>

```
Kali Linux
    |
    | Private Lab Network
    |
Metasploitable 2
```

This keeps the lab isolated and allows the two VMs to communicate.

8. Verify Connectivity

Checked the IP address of Kali Linux:

>ip addr

Checked the IP address of Metasploitable 2:

>ifconfig


Then tested connectivity from Kali:

>ping

<p align="center">
  <img src="screenshots/connectivity.png" width="900">
</p>

---

```
📁 Repository Structure
task-1/
│
├── README.md
│
└── screenshots/
    ├── 01-virtualbox.png
    ├── 02-kali-iso.png
    ├── 03-kali-vm-settings.png
    ├── 04-kali-desktop.png
    ├── 05-metasploitable.png
    ├── 06-metasploitable-settings.png
    └── 07-connectivity.png
```

---

### ✅ Lab Status
 VirtualBox installed
 Kali Linux 2026 installed
 Kali VM configured
 Kali user configured
 Metasploitable 2 installed
 Metasploitable 2 configured
 Private lab network configured
 Connectivity tested

---
🔒 Safety

The lab is intended for authorized cybersecurity training only. Metasploitable 2 is intentionally vulnerable and should be kept within an isolated lab network.
