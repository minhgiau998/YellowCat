import whois
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        
        def print_colored(key, value):
            print(f"{good}{Fore.LIGHTGREEN_EX} {key}: {Fore.YELLOW}{value}")

        if isinstance(domain_info, dict):
            for key, value in domain_info.items():
                if isinstance(value, list):
                    value = ', '.join(str(v) for v in value)
                print_colored(key, value)
        else:
            print(domain_info)
    
    except Exception as e:
        print(f"{bad}{Fore.RED} An error occurred: {e}")

