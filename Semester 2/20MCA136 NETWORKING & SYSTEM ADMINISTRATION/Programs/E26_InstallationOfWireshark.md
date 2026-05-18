

# 📘 README

<div align="center">

# 🖥️ E26_InstallationOfWireshark

### NSA Lab – Installation of Wireshark

</div>

---

# 🎯 Aim

To install and configure Wireshark in Linux and analyze network packets using packet capturing techniques.

---

# 📘 Introduction

Wireshark is a free and open-source network packet analyzer used for:

* network troubleshooting
* protocol analysis
* network monitoring
* cybersecurity analysis
* packet inspection

Wireshark captures packets flowing through a network interface and displays detailed protocol-level information.

It is widely used by:

* network administrators
* ethical hackers
* cybersecurity professionals
* protocol developers
* system administrators

---

# 🧠 What is Packet Analysis?

Packet analysis is the process of:

* capturing network packets
* inspecting data transfer
* analyzing communication between systems

Each packet contains:

* source address
* destination address
* protocol information
* payload data

Packet analysis helps detect:

* network errors
* attacks
* connectivity issues
* abnormal traffic

---

# 🦈 What is Wireshark?

Wireshark is a GUI-based packet analyzer that captures and analyzes network traffic in real time.

## 📌 Features of Wireshark

* Real-time packet capture
* Deep protocol inspection
* Live traffic monitoring
* Packet filtering
* Protocol decoding
* Export and save captures
* Cross-platform support

---

# 🌐 Uses of Wireshark

Wireshark is used for:

| Purpose                 | Description                 |
| ----------------------- | --------------------------- |
| Network Troubleshooting | Diagnose network problems   |
| Security Analysis       | Detect suspicious traffic   |
| Protocol Development    | Analyze protocol behavior   |
| Learning Networking     | Understand packet flow      |
| Performance Analysis    | Monitor traffic performance |

---

# ⚙️ System Requirements

Before installation ensure:

| Requirement         | Purpose           |
| ------------------- | ----------------- |
| Ubuntu/Linux        | Operating System  |
| Internet Connection | Download packages |
| Sudo Privileges     | Install software  |
| Network Interface   | Capture packets   |

---

# 🪜 Step 1: Update Package Repository

Update package repository to fetch latest package information.

## 📌 Command

```bash id="m4x8qp"
sudo apt update
```

---

# 📌 Purpose

* Updates package index
* Downloads latest repository information
* Prevents installation issues

---

# 📦 Step 2: Install Wireshark

Install Wireshark using apt package manager.

## 📌 Command

```bash id="v7n2zk"
sudo apt install wireshark
```

---

# 📌 During Installation

The installer may ask:

```text id="q9p1wr"
Should non-superusers be able to capture packets?
```

Choose:

```text id="x5m2vq"
Yes
```

This allows normal users to capture packets.

---

# 🧠 What Happens During Installation?

The following components are installed:

* Wireshark GUI
* tshark command-line tool
* protocol analyzers
* capture libraries

---

# 👥 Step 3: Configure Wireshark Group

To allow non-root users to capture packets, add current user to the Wireshark group.

## 📌 Command

```bash id="k3v8zp"
sudo usermod -aG wireshark $USER
```

---

# 📌 Explanation

| Option  | Meaning                |
| ------- | ---------------------- |
| `-a`    | Append user            |
| `-G`    | Add to group           |
| `$USER` | Current logged-in user |

---

# 🔄 Step 4: Refresh Group Membership

After adding the user to the group:

* logout and login again

OR run:

```bash id="p7n1wr"
newgrp wireshark
```

---

# ▶️ Step 5: Start Wireshark

Launch Wireshark application.

## 📌 Command

```bash id="t4m9qx"
sudo wireshark
```

---

# 🖥️ Wireshark Interface Components

| Component           | Function             |
| ------------------- | -------------------- |
| Menu Bar            | Access features      |
| Toolbar             | Quick controls       |
| Packet List Pane    | Displays packets     |
| Packet Details Pane | Detailed packet info |
| Packet Bytes Pane   | Raw packet data      |

---

# 🌐 Step 6: Select Network Interface

Choose the network interface to capture traffic.

## 📌 Common Interfaces

| Interface | Purpose  |
| --------- | -------- |
| eth0      | Ethernet |
| wlan0     | WiFi     |
| lo        | Loopback |

---

# 📡 Step 7: Start Packet Capture

Click the:

```text id="v8x2zk"
Green Shark Fin Icon
```

Wireshark begins capturing live packets.

---

# 📦 Types of Captured Packets

Wireshark can capture:

* HTTP packets
* HTTPS packets
* TCP packets
* UDP packets
* DNS requests
* ICMP packets
* ARP packets

---

# 🔍 Step 8: Analyze Captured Packets

Wireshark provides:

* filters
* protocol dissectors
* statistics
* flow analysis

---

# 📌 Common Display Filters

| Filter               | Purpose      |
| -------------------- | ------------ |
| `http`               | HTTP traffic |
| `tcp`                | TCP packets  |
| `udp`                | UDP packets  |
| `dns`                | DNS traffic  |
| `icmp`               | Ping packets |
| `ip.addr == x.x.x.x` | Specific IP  |

---

# 📌 Example Filters

```text id="m2q7vp"
http
```

Displays HTTP packets.

---

```text id="x9p4wr"
tcp.port == 80
```

Displays traffic on port 80.

---

```text id="q5n8zk"
ip.addr == 192.168.1.1
```

Displays packets from specific IP.

---

# 📊 Packet Information

Each packet contains:

| Field          | Description            |
| -------------- | ---------------------- |
| Source IP      | Sender address         |
| Destination IP | Receiver address       |
| Protocol       | Communication protocol |
| Length         | Packet size            |
| Info           | Packet summary         |

---

# ⏹️ Step 9: Stop Packet Capture

Click the:

```text id="u4m7xp"
Red Square Stop Button
```

to stop capturing packets.

---

# 💾 Step 10: Save Captured Packets

To save packet capture:

## 📌 Menu Path

```text id="p8x2vq"
File → Save
```

---

# 📌 Capture File Formats

| Format  | Description             |
| ------- | ----------------------- |
| .pcap   | Packet capture file     |
| .pcapng | Extended capture format |

---

# 🧩 Command-Line Wireshark Tool

Wireshark also provides:

```text id="v3n7zk"
tshark
```

for terminal-based packet capture.

---

# 📌 Example tshark Command

```bash id="m6q1wr"
sudo tshark
```

---

# 🔐 Security Uses of Wireshark

Wireshark helps identify:

* malicious traffic
* suspicious connections
* unauthorized access
* packet flooding
* protocol attacks

---

# ⚠️ Limitations of Wireshark

* Cannot decrypt encrypted traffic without keys
* Large captures consume memory
* Requires network knowledge
* Promiscuous mode may require permissions

---

# 📂 Wireshark Workflow

```text id="x2v8qp"
Network Traffic
       ↓
Network Interface
       ↓
Wireshark Capture
       ↓
Packet Analysis
       ↓
Filtering and Inspection
```

---

# ✅ Advantages of Wireshark

* Free and open-source
* Powerful protocol analyzer
* Real-time traffic analysis
* Easy GUI interface
* Supports many protocols
* Useful for cybersecurity

---

# ❌ Disadvantages

* Requires networking knowledge
* Large captures may slow system
* Complex for beginners initially

---

# 📚 Viva Questions

## 1️⃣ What is Wireshark?

Wireshark is a network packet analyzer.

---

## 2️⃣ What is packet capture?

Packet capture is collecting network packets for analysis.

---

## 3️⃣ What is protocol analysis?

Protocol analysis is examining communication protocols in packets.

---

## 4️⃣ What is the use of filters in Wireshark?

Filters help display specific packets.

---

## 5️⃣ What is promiscuous mode?

Promiscuous mode allows capturing all network packets.

---

## 6️⃣ What is the purpose of `sudo usermod -aG wireshark $USER`?

It adds user to Wireshark group.

---

## 7️⃣ What are TCP and UDP?

They are transport layer communication protocols.

---

## 8️⃣ What is a `.pcap` file?

It stores captured packet data.

---

## 9️⃣ What is tshark?

tshark is the command-line version of Wireshark.

---

## 🔟 Why is Wireshark important?

It helps monitor, troubleshoot, and secure networks.

---

# 🎓 Result

Thus, Wireshark was installed and configured successfully, and network packets were captured and analyzed using packet analysis techniques.
