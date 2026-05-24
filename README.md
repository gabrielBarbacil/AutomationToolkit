# AutomationToolkit

> A set of tools and scripts focused on automating repetitive pentesting processes, from initial reconnaissance to reporting.

---

## Overview

AutomationToolkit is a personal collection of Python scripts built from scratch for offensive security workflows. Each tool is designed to be modular, CLI-driven, and easy to extend. The toolkit is actively growing alongside a structured Python learning path focused on pentesting automation.

---

## Tools

### 🔍 Port Scanner — `fase2-redes/scanner_final.py`

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

## Project Structure

```
AutomationToolkit/
├── fase2-redes/
│   ├── scanner.py           # Basic sequential port scanner
│   ├── scanner_v2.py        # Threading with manual lock
│   ├── scanner_v3.py        # ThreadPoolExecutor (controlled concurrency)
│   └── scanner_final.py     # Full scanner — argparse + threads + JSON output
│
├── fase3-scripting/
│   ├── fuzzer.py            # Directory fuzzer — argparse + wordlist + log
│   └── wordlist.txt         # Sample wordlist
│
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
# Scan localhost ports 1-1024 with 100 threads
python scanner_final.py -t 127.0.0.1 -p 1-1024 -w 100

# Fuzz a target with a custom wordlist
python fuzzer.py -u http://10.10.10.5 -w /usr/share/wordlists/dirb/common.txt

# Scan a full port range aggressively
python scanner_final.py -t 192.168.1.1 -p 1-65535 -w 500
```

---

## Disclaimer

This toolkit is intended for **authorized security testing and educational purposes only**. Do not use these tools against systems you do not own or have explicit permission to test. The author is not responsible for any misuse.

---

## Roadmap

- [x] TCP port scanner with banner grabbing
- [x] Multithreaded scanner with concurrency control
- [x] HTTP directory fuzzer with wordlist support
- [ ] SSH / HTTP brute force
- [ ] Web scraper and response parser
- [ ] Subdomain enumerator
- [ ] Full recon toolkit with unified reporting

---

*Built while learning Python for offensive security — one script at a time.*
