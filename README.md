# Automation Toolkit

> A set of tools and scripts focused on automating repetitive pentesting processes, from initial reconnaissance to reporting.

---

## Overview

AutomationToolkit is a personal collection of Python scripts built from scratch for offensive security workflows. Each tool is designed to be modular, CLI-driven, and easy to extend. The toolkit is actively growing alongside a structured Python learning path focused on pentesting automation.

---

## Toolkit— Unified entry point

All tools accessible from a single CLI with subcommands, similar to gobuster.

```bash
python main.py scan   -t 192.168.1.1 -p 1-1024
python main.py fuzz   -u http://192.168.1.1 -w wordlist.txt
python main.py brute  -u http://192.168.1.1/login -U users.txt -w passwords.txt
python main.py spider -u http://192.168.1.1
```

## Tools
### 🔍 Port Scanner — `fase2-network/scanner_final.py`

Multithreaded TCP port scanner with banner grabbing and JSON output.


| Argument | Description |
|----------|-------------|
| `-t` | Target IP |
| `-p` | Port range (e.g. `1-1024`) |
| `-w` | Number of concurrent threads (default: 100) |

**Features:**
- Concurrent scanning via `ThreadPoolExecutor`
- Banner grabbing on open ports
- Results exported to `resultados.json`

---

### 🌐 Directory Fuzzer — `fase3-scripting/fuzzer.py`

HTTP directory fuzzer with wordlist support, status code filtering and persistent log.


| Argument | Description |
|----------|-------------|
| `-u` | Target base URL |
| `-w` | Path to wordlist file |

**Features:**
- Filters 404 responses — only reports hits
- Supports any HTTP target
- Appends results to `fuzzer_log.txt` for audit trail
- Handles connection errors and timeouts gracefully

---

### 🔑 HTTP Brute Force — `python/fase3-scripting/brute_http.py`

HTTP login brute force with user and password wordlists.



| Argument | Description |
|----------|-------------|
| `-u` | Login endpoint URL |
| `-U` | File with usernames |
| `-w` | File with passwords |


**Features:**
- Supports username + password wordlists
- Detects success by HTTP status code
- Saves result to passwd_crack.json

---

### 🔐 SSH Brute Force — `python/fase3-scripting/brute_ssh.py`

SSH brute force using paramiko with rate limiting evasion.



| Argument | Description |
|----------|-------------|
| `-t` | Target IP |
| `-U` | File with usernames |
| `-w` | File with passwords |


**Features:**
- Detects success via AuthenticationException
- Built-in delay to evade rate limiting
- Handles connection resets gracefully

---

### 🕷️ Web Spider — `python/fase3-scripting/spider.py`

Recursive web spider that maps the full structure of a web application.




| Argument | Description |
|----------|-------------|
| `-U` | Base URL to spider |


**Features:**
- Recursively follows all internal links
- Deduplicates visited URLs with a set
- Reports status codes for each page
- Useful for finding exposed files and directories

---

## Project Structure

```
AutomationToolkit/
├── toolkit/
│   ├── main.py              # Unified entry point — subcommands
│   ├── scanner.py           # TCP connect scanner module
│   ├── fuzzer.py            # Directory fuzzer module
│   ├── brute.py             # HTTP brute force module
│   ├── spider.py            # BFS web spider module
│   └── utils.py             # Shared utilities (in progress)
│
├── python/
│   ├── fase2-network/         # Standalone scanner scripts (v1-v3 + final)
│   └── fase3-scripting/     # Standalone tool scripts
│
├── bash/                    # Coming soon
└── README.md
```

---

## Requirements

```bash
pip install requests beautifulsoup4 paramiko flask
```



---

## Disclaimer

This toolkit is intended for **authorized security testing and educational purposes only**. Do not use these tools against systems you do not own or have explicit permission to test. The author is not responsible for any misuse.

---

## Roadmap

- [x] TCP port scanner with banner grabbing
- [x] Multithreaded scanner with concurrency control
- [x] HTTP directory fuzzer with wordlist support
- [x] HTTP login brute force
- [x] SSH brute force with rate limiting evasion
- [x] Recursive web spider
- [x] Modular architecture with unified entry point
- [x]  All tools integrated as subcommands
- [ ] utils.py — shared reporting and output functions
- [ ] Automated HTML reporting
- [ ] OOP refactor — Scanner, Fuzzer, BruteForcer, Spider classes
- [ ] Scapy — SYN scan, ARP spoofing, packet crafting
- [ ] Living off the land — stdlib-only modules (urllib, html.parser)
- [ ] Bash scripts for post-exploitation automation

---

*Built while learning Python for offensive security — one script at a time.*
