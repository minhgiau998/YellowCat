import dns.resolver
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_dns_lookup_info(domain):
    try:
        # Lookup A record
        a_result = dns.resolver.resolve(domain, 'A')
        print(f"{run}{Fore.WHITE} A record lookup results for {domain}:")
        for ipval in a_result:
            print(f"{good}{Fore.LIGHTGREEN_EX} IP Address: {ipval.to_text()}")

        # Lookup CNAME record
        try:
            cname_result = dns.resolver.resolve(domain, 'CNAME')
            print(f"{run}{Fore.LIGHTBLUE_EX} CNAME record lookup results for {domain}:")
            for cnameval in cname_result:
                print(f"{good}{Fore.LIGHTBLUE_EX} CNAME: {cnameval.target}")
        except dns.resolver.NoAnswer:
            print(f"{bad}{Fore.RED} No CNAME record found for {domain}.")

        # Lookup MX record
        try:
            mx_result = dns.resolver.resolve(domain, 'MX')
            print(f"{run}{Fore.WHITE} MX record lookup results for {domain}:")
            for mxval in mx_result:
                print(f"{good}{Fore.LIGHTBLUE_EX} MX Record: {mxval.exchange}")
        except dns.resolver.NoAnswer:
            print(f"{bad}{Fore.RED} No MX record found for {domain}.")
        
    except dns.resolver.NXDOMAIN:
        print(f"{bad}{Fore.RED} Error: {domain} does not exist.")
    except dns.resolver.Timeout:
        print(f"{bad}{Fore.RED} Error: The request timed out.")
    except dns.resolver.NoNameservers:
        print(f"{bad}{Fore.RED} Error: No nameservers available.")
    except dns.exception.DNSException as e:
        print(f"{bad}{Fore.RED} Error: {e}")
