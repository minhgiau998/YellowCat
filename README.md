<h1 align="center">
  <br>
  <a href="https://github.com/minhgiau998/YellowCat"><img width="200" height="200" src="https://raw.githubusercontent.com/minhgiau998/YellowCat/master/assets/yellowcat-logo.svg" alt="YellowCat"></a>
  <br>
  YellowCat
  <br>
</h1>

<h4 align="center">An exceptionally fast crawler optimized for OSINT (Open Source Intelligence).</h4>

<p align="center">
  <a href="https://github.com/minhgiau998/YellowCat/releases">
    <img src="https://img.shields.io/github/release/minhgiau998/YellowCat.svg">
  </a>
  <a href="https://github.com/minhgiau998/YellowCat/issues?q=is%3Aissue+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-closed-raw/minhgiau998/YellowCat.svg">
  </a>
</p>

## Screenshots

```text
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((--------

[01] Whois
[02] Traceroute
[03] DNS Lookup
[04] Reverse DNS
[05] GeoIP Lookup
[06] Port Scan
[07] Page Links
[08] HTTP Header
[09] Email Header
[10] SQLmap
[11] Subdomain Scanner
[12] Robots.txt Scanner
[13] CMS Detector
[14] Directory Fuzzer
[99] Exit

Enter your choice [1-99]:
```

## Features

- **Whois**: Provides detailed information about domain registration, including owner details, registration date, and expiration date.
- **Traceroute**: Tracks the path of data packets from a computer to the target server, helping to identify intermediary points and detect network issues.
- **DNS Lookup**: Queries the domain name system to retrieve information about the IP address corresponding to a domain name.
- **Reverse DNS**: Converts an IP address back to a domain name, helping to identify the domain associated with a specific IP address.
- **GeoIP Lookup**: Determines the geographical location of an IP address, providing information about the country, city, and internet service provider.
- **Port Scan**: Checks for open ports on the target server, helping to identify running services and potential security vulnerabilities.
- **Page Links**: Collects all links on a specific webpage, helping to identify the structure and related resources of the website.
- **HTTP Header**: Analyzes HTTP headers from requests and responses between the client and server, providing information about the server, connection status, and security settings.
- **Email Header**: Analyzes email headers to determine the origin, path, and other related information, helping to detect phishing attacks and email security issues.
- **SQLmap**: Automates the process of detecting and exploiting SQL injection vulnerabilities in web applications.
- **Subdomain Scanner**: Identifies subdomains associated with a domain using passive sources (crt.sh).
- **Robots.txt Scanner**: Analyzes the robots.txt file to identify hidden paths and disallowed directories.
- **CMS Detector**: Identifies the technology stack (WordPress, Joomla, Drupal) used by a website.
- **Directory Fuzzer**: Identifies hidden directories and files using a wordlist.

## Roadmap

I am actively working on making YellowCat the ultimate reconnaissance tool. Here is what we have planned for future releases:

- [x] **Directory Fuzzing (DirBuster)**: Implement a brute-force module to find hidden directories (e.g., `/admin`, `/backup`, `/config`) using common wordlists.
- [ ] **WAF Detection**: Add capability to detect Web Application Firewalls (Cloudflare, Akamai, AWS WAF) to understand target defenses.
- [ ] **Multi-threaded Port Scanning**: Upgrade the current port scanner to use Python threading for significantly faster execution speeds.
- [ ] **CVE Lookup**: Integrate a vulnerability database lookup to search for known CVEs based on detected service versions.
- [ ] **Report Generation**: Add functionality to export scan results to HTML, PDF, or JSON formats for documentation.
- [ ] **Shodan Integration**: Add API support for Shodan to perform passive IP analysis without direct interaction.
- [ ] **Password Bruteforcing**: Implement a password cracking module to attempt to crack weak passwords using common wordlists.
- [ ] **Advanced Fingerprinting**: Enhance the fingerprinting capabilities to identify more sophisticated web technologies and frameworks.
- [ ] **Custom Payloads**: Allow users to define custom payloads for specific targets or scenarios.
- [ ] **Custom Malware Payloads**: Implement a module to analyze custom malware samples for indicators of compromise (IoCs).

## Installation

Clone the project:

```bash
git clone https://github.com/minhgiau998/YellowCat.git
```

Go to the project directory:

```bash
cd YellowCat
```

Create a virtual environment:

```bash
py -m venv venv
```

Activate the virtual environment:

*Windows:*
```bash
.\venv\Scripts\activate
```

*Linux/Mac:*
```bash
source venv/bin/activate
```

Install library dependencies:

```bash
py -m pip install -r requirements.txt
```

Start the project:

```bash
py yellowcat.py
```

## Demo

[![asciicast](https://asciinema.org/a/bDURqdryjnCyNuRD9LSNce631.svg)](https://asciinema.org/a/bDURqdryjnCyNuRD9LSNce631)

## Support

For support, email minhgiau04041998@gmail.com or join our Discord channel.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@minhgiau998](https://www.github.com/minhgiau998)
