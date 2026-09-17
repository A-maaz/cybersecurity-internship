# 🔍 Nmap Network Reconnaissance Report

## 📌 Scan Overview
* **Initiated on:** Fri Aug 28 19:50:46 2026
* **Completed on:** Fri Aug 28 19:51:52 2026 (Scan duration: 65.39 seconds)
* **Command Executed:** `nmap -sS -sV -O -oN nmap_scan.txt 10.0.2.4`
* **Target IP:** `10.0.2.4`
* **Host Status:** Up (0.0023s latency, 1 hop)
* **MAC Address:** `08:00:27:E0:77:F0` (Oracle VirtualBox virtual NIC)

---

## 💻 Target Operating System Details
* **Device Type:** General purpose
* **Running OS:** Linux 2.6.X
* **OS CPE:** `cpe:/o:linux:linux_kernel:2.6`
* **OS Details:** Linux 2.6.9 - 2.6.33 (Ubuntu 8.04 LTS / generic Linux/Unix)

---

## 🚪 Port Scan Summary
* **Total Scanned Ports:** 1,000
* **Closed Ports:** 977 (filtered/reset)
* **Open Ports:** 23

### Discovered Open Ports & Services Table

| Port | Protocol | Service | Version / Details |
| :--- | :--- | :--- | :--- |
| **21** | TCP | ftp | `vsftpd 2.3.4` |
| **22** | TCP | ssh | `OpenSSH 4.7p1 Debian 8ubuntu1` (protocol 2.0) |
| **23** | TCP | telnet | `Linux telnetd` |
| **25** | TCP | smtp | `Postfix smtpd` |
| **53** | TCP | domain | `ISC BIND 9.4.2` |
| **80** | TCP | http | `Apache httpd 2.2.8 ((Ubuntu) DAV/2)` |
| **111** | TCP | rpcbind | `2 (RPC #100000)` |
| **139** | TCP | netbios-ssn | `Samba smbd 3.X - 4.X` (workgroup: WORKGROUP) |
| **445** | TCP | netbios-ssn | `Samba smbd 3.X - 4.X` (workgroup: WORKGROUP) |
| **512** | TCP | exec? | Unverified / proprietary exec service |
| **513** | TCP | login | `rlogin` service |
| **514** | TCP | tcpwrapped | TCP wrapper protected service |
| **1099** | TCP | java-rmi | `GNU Classpath grmiregistry` |
| **1524** | TCP | bindshell | `Metasploitable root shell` (backdoor port) |
| **2049** | TCP | nfs | `2-4 (RPC #100003)` |
| **2121** | TCP | ftp | `ProFTPD 1.3.1` |
| **3306** | TCP | mysql | `MySQL 5.0.51a-3ubuntu5` |
| **5432** | TCP | postgresql | `PostgreSQL DB 8.3.0 - 8.3.7` |
| **5900** | TCP | vnc | `VNC (protocol 3.3)` |
| **6000** | TCP | X11 | X11 display server *(access denied)* |
| **6667** | TCP | irc | `UnrealIRCd` |
| **8009** | TCP | ajp13 | `Apache Jserv (Protocol v1.3)` |
| **8180** | TCP | http | `Apache Tomcat/Coyote JSP engine 1.1` |

---

## 📋 Additional Service Information
* **Hosts Identifiers:** `metasploitable.localdomain`, `irc.Metasploitable.LAN`
* **Underlying OS Environment:** Unix / Linux

---

## 🔎 Key Security Observations
1. **Massive Attack Surface:** The scan highlights 23 active network ports, exposing a broad variety of legacy and unpatched network services.
2. **Plaintext Administrative Protocols:** Services like Telnet (port 23), rlogin (port 513), and multiple FTP daemons (ports 21, 2121) handle authentication over unencrypted channels, leaving credentials vulnerable to packet sniffing.
3. **High-Risk Backdoors & Shells:** Port 1524 (`bindshell`) directly exposes a pre-configured root shell, which is a known vulnerability footprint of the Metasploitable 2 lab environment.
4. **Exposed Databases:** Both MySQL (port 3306) and PostgreSQL (port 5432) are directly accessible via network sockets, increasing exposure to brute-force or injection attacks.
