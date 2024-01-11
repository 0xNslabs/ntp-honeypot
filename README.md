# Simple NTP Honeypot Server

## Introduction
The Simple NTP Honeypot Server is a script designed for cybersecurity experts and enthusiasts to study NTP-based network interactions. Crafted in Python using the Twisted framework, this tool simulates an NTP server, effectively logging unauthorized access and interactions. It serves as an essential resource for understanding NTP security vulnerabilities and potential exploitation methods.

## Features
- **Low-Interaction Honeypot**: Imitates an NTP server, safely capturing and logging interaction data.
- **Flexible Configuration**: Customizable settings for host and port, adjustable via command-line parameters.
- **Detailed Interaction Logging**: Documents all NTP requests and responses, offering insights into potential threats.
- **Real-Time Traffic Monitoring**: Instantaneously logs NTP communication for quick anomaly detection and analysis.
- **Educational and Research Utility**: Excellent for exploring NTP security and network reconnaissance techniques.

## Requirements
- Python 3.x
- Twisted Python library

## Installation
To install and configure the NTP honeypot server, execute the following steps:

```bash
git clone https://github.com/0xNslabs/ntp-honeypot.git
cd ntp-honeypot
pip install twisted
```

## Usage
Launch the server using the following command, with optional arguments for host and port. By default, the server binds to all interfaces (0.0.0.0) on port 123.

```bash
python3 ntp.py --host 0.0.0.0 --port 123
```

## Logging
The server logs all NTP interactions in ntp_honeypot.log, providing detailed accounts of requests and client information.

## Simple NTP Honeypot In Action
![Simple NTP Honeypot in Action](https://raw.githubusercontent.com/0xNslabs/ntp-honeypot/main/PoC.png)
*This image demonstrates the Simple NTP Honeypot Server in action, capturing real-time NTP requests and client interactions.*

## Other Simple Honeypot Services

Check out the other honeypot services for monitoring various network protocols:

- [DNS Honeypot](https://github.com/0xNslabs/dns-honeypot) - Monitors DNS interactions.
- [FTP Honeypot](https://github.com/0xNslabs/ftp-honeypot) - Simulates an FTP server.
- [LDAP Honeypot](https://github.com/0xNslabs/ldap-honeypot) - Mimics an LDAP server.
- [NTP Honeypot](https://github.com/0xNslabs/ntp-honeypot) - Monitors Network Time Protocol interactions.
- [PostgreSQL Honeypot](https://github.com/0xNslabs/postgresql-honeypot) - Simulates a PostgreSQL database server.
- [SIP Honeypot](https://github.com/0xNslabs/sip-honeypot) - Monitors SIP (Session Initiation Protocol) interactions.
- [SSH Honeypot](https://github.com/0xNslabs/ssh-honeypot) - Emulates an SSH server.
- [TELNET Honeypot](https://github.com/0xNslabs/telnet-honeypot) - Simulates a TELNET server.

## Security and Compliance
- **Caution**: Utilize this honeypot in secure and controlled environments, primarily for educational and research purposes.
- **Compliance**: Ensure that deployment aligns with local and international legal and ethical guidelines.

## License
This project is licensed under the MIT License. More details can be found in the LICENSE file.