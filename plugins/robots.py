import requests
from colorama import Fore

def print_robots_info(url):
    if not url.startswith("http"):
        url = "http://" + url

    target = url.rstrip("/") + "/robots.txt"

    print(f"{Fore.BLUE}[~] Checking: {Fore.WHITE}{target}")

    try:
        res = requests.get(target, timeout=10)
        if res.status_code == 200:
            print(f"{Fore.GREEN}[+] robots.txt found!\n")
            for line in res.text.splitlines():
                if "Disallow" in line:
                    print(f"{Fore.RED}{line}") # Red for forbidden paths
                elif "Allow" in line:
                    print(f"{Fore.GREEN}{line}") # Green for allowed
                else:
                    print(f"{Fore.WHITE}{line}")
        else:
            print(f"{Fore.YELLOW}[-] No robots.txt found (Status: {res.status_code})")
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}")
