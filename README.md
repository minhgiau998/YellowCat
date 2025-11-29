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
  <a href="https://pypi.org/project/yellowcat/">
    <img src="https://img.shields.io/badge/pypi-@yellowcat-red.svg?style=flat-square" alt="pypi">
  </a>
  <a href="https://github.com/minhgiau998/YellowCat/issues?q=is%3Aissue+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-closed-raw/minhgiau998/YellowCat.svg">
  </a>
</p>

## Screenshots

```
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((-------- version 1.0.0

[01] Whois
[02] Traceroute
[03] DNS Lookup
[04] Reverse DNS
[05] GeoIP Lookup
[06] Port Scan
[07] Page Links
[08] HTTP Header
[09] Email Header
[11] Subdomain Scanner
[12] Robots.txt Scanner
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
- **Subdomain Scanner**: Identifies subdomains associated with a domain, helping to discover hidden resources and potential security vulnerabilities.
- **Robots.txt Scanner**: Analyzes the robots.txt file of a website to identify disallowed paths and potential security vulnerabilities.

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

```bash
source venv/Scripts/activate
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
