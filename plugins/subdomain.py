import requests
from colorama import Fore, Style

def print_subdomain_info(domain):
    """
    Scans for subdomains using certificate transparency logs (crt.sh)
    """
    print(f"{Fore.BLUE}[~] Searching for subdomains for: {Fore.WHITE}{domain}")
    print(f"{Fore.YELLOW}[INFO] Querying crt.sh database (this is passive and stealthy)...")

    # Clean the domain input just in case
    domain = domain.replace("http://", "").replace("https://", "").strip("/")

    url = f"https://crt.sh/?q=%.{domain}&output=json"

    try:
        response = requests.get(url, timeout=20)

        if response.status_code != 200:
            print(f"{Fore.RED}[-] Error retrieving data from crt.sh")
            return

        data = response.json()

        # Use a set to store unique subdomains (crt.sh returns duplicates)
        subdomains = set()

        for entry in data:
            name_value = entry['name_value']
            # Sometimes results have multiple lines
            parts = name_value.split('\n')
            for part in parts:
                if part.endswith(domain) and "*" not in part:
                    subdomains.add(part)

        if len(subdomains) > 0:
            print(f"\n{Fore.GREEN}[+] Found {len(subdomains)} unique subdomains:\n")
            for sub in sorted(subdomains):
                print(f"{Fore.CYAN} - {Fore.WHITE}{sub}")
        else:
            print(f"{Fore.YELLOW}[!] No subdomains found in certificate logs.")

    except Exception as e:
        print(f"{Fore.RED}[-] An error occurred: {str(e)}")
