# 🔍 Simple Python Port Scanner

A lightweight and educational TCP port scanner written in Python. This tool scans a target host for open ports, identifies common services, and retrieves basic banners where available.

>  This project is intended for educational purposes only.

### USEAGE
port *host* *port1* *port2*

### Examples
help
port 127.0.0.1 20 100
port scanme.nmap.org 1 1024
port example.com 80 443



##  Overview

This port scanner allows users to:
- Scan a specified range of TCP ports.
- Identify open ports on a target system.
- Detect common services running on those ports.
- Retrieve server banners if available.
- Practice fundamental networking and cybersecurity concepts.


---

##  Features

-  TCP port scanning
-  Hostname or IP address support
-  Adjustable scanning speed via socket timeouts
-  Service detection using standard port mappings
-  Basic banner grabbing
-  Command-line interface
-  Built for educational and learning purposes

---

##  Requirements

- Python 3.x
- No external libraries required

---
