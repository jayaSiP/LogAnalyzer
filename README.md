# 🛡️ Log Analyzer

## Project Overview

**Log Analyzer** is a Python tool that turns raw web server logs into cybersecurity insights. It identifies suspicious activity like failed logins, sensitive endpoint access, and unusual request patterns, then generates a clear, human-readable report.

---

## 🚀 Features

* Parse web server logs into structured data.
* Detect suspicious activity:

  * Failed login attempts (HTTP 401 on `/login`)
  * Access to sensitive endpoints (`/admin`, `/config`, `/.env`, `/wp-admin`, `/phpmyadmin`)
  * High request volume per IP
  * HTTP 404 scanning activity
  * Server errors (HTTP 5xx responses)
  * Unusual HTTP methods (anything other than GET or POST)
* Generate readable reports summarizing findings.

---

## 📂 File Structure

| File             | Description                                       |
| ---------------- | ------------------------------------------------- |
| `parser.py`      | Reads and parses log files                        |
| `detector.py`    | Functions to analyze logs for suspicious activity |
| `report.py`      | Generates a human-readable report                 |
| `main.py`        | Runs the log analyzer                             |
| `sample_log.txt` | Example log file for testing                      |

---

## ⚡ Getting Started

### Prerequisites

* Python 3.x installed on your machine.

### Installation & Usage

1. Clone this repository:

```bash
git clone https://github.com/SantaLauk/Log-Analyzer.git
cd Log-Analyzer
```

2. Run the main program:

```bash
python main.py
```

3. The program will parse the log file and print a report of findings.

---

## 📋 Example Report

```text
===== LOG ANALYSIS REPORT =====

Total Requests Per IP:
192.168.1.11: 12
192.168.1.10: 11
192.168.1.13: 3

Failed Login Attempts:
192.168.1.17: 3 failed logins
192.168.1.10: 2 failed logins

Sensitive Endpoint Access:
192.168.1.12: accessed ['/admin']
192.168.1.15: accessed ['/config']

High Request Volume:
192.168.1.11: 12 requests
192.168.1.10: 11 requests

404 Scanning Activity:
192.168.1.13: 3 HTTP 404 responses

Server Errors (5xx):
192.168.1.16: 2 server errors

Suspicious HTTP Methods:
192.168.1.14: ['DELETE']

===== END OF REPORT =====
```

---

## 🎯 Future Improvements

* Time-based detection for **brute force login attempts**.
* Detection of **endpoint scanning and enumeration patterns**.
* Combined **suspicion scoring** (mini SIEM style).
* Optional **visualization** of suspicious activity.

---

## 📜 License

MIT License – free to use for learning and portfolio purposes.

---
