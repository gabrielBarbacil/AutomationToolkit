# Automation Toolkit

> A set of tools and scripts focused on automating repetitive pentesting processes, from initial reconnaissance to reporting.

---

## Overview

AutomationToolkit is a personal collection of Python scripts built from scratch for offensive security workflows. Each tool is designed to be modular, CLI-driven, and easy to extend. The toolkit is actively growing alongside a structured Python learning path focused on pentesting automation.

---

## Tools

### 🔍 Port Scanner — `fase2-network/scanner_final.py`

Multithreaded TCP port scanner with banner grabbing and JSON output.

```bash
python scanner_final.py -t 192.168.1.1 -p 1-1024 -w 200
```

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

```bash
python fuzzer.py -u http://target.com -w wordlist.txt
```

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

```bash
python brute_http.py -u http://target.com/login -U users.txt -w passwords.txt
```

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

```bash
python brute_ssh.py -t 192.168.1.1 -U users.txt -w passwords.txt
```

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

```bash
python spider.py -u http://target.com
```


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
├── python/
│   ├── fase2-network/
│   │   ├── scanner.py           # Basic sequential port scanner
│   │   ├── scanner_v2.py        # Threading with manual lock
│   │   ├── scanner_v3.py        # ThreadPoolExecutor
│   │   └── scanner_final.py     # Full scanner — argparse + threads + JSON
│   │
│   └── fase3-scripting/
│       ├── fuzzer.py            # Directory fuzzer
│       ├── brute_http.py        # HTTP login brute force
│       ├── brute_ssh.py         # SSH brute force
│       ├── spider.py            # Recursive web spider
│       └── wordlist.txt         # Sample wordlist
│
├── bash/                        # Coming soon
└── README.md
```

---

## Requirements

```bash
pip install requests
```

All other modules (`socket`, `threading`, `argparse`, `json`) are part of the Python standard library.

**Python version:** 3.8+

---

## Usage Examples

```bash
# Full recon workflow
python scanner_final.py -t 192.168.1.1 -p 1-1024 -w 100
python spider.py -u http://192.168.1.1
python fuzzer.py -u http://192.168.1.1 -w wordlist.txt
python brute_http.py -u http://192.168.1.1/login -U users.txt -w passwords.txt
python brute_ssh.py -t 192.168.1.1 -U users.txt -w passwords.txt
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
- [ ] Scapy — packet crafting and network evasion
- [ ] Modular toolkit with unified entry point
- [ ] Automated HTML/PDF reporting
- [ ] Subdomain enumerator
- [ ] Bash scripts for post-exploitation automation

---

*Built while learning Python for offensive security — one script at a time.*
