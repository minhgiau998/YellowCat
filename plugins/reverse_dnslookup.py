import dns.reversename
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_reverse_dns_lookup_info(ip_address):
    try:
        # Get the PTR record for the IP address
        addr = dns.reversename.from_address(ip_address)
        ptr_result = dns.resolver.resolve(addr, 'PTR')
        print(f"{run}{Fore.WHITE} PTR record lookup results for {ip_address}:")
        for ptrval in ptr_result:
            print(f"{good}{Fore.LIGHTGREEN_EX} Hostname: {ptrval}")
    except dns.resolver.NXDOMAIN:
        print(f"{bad}{Fore.RED} Error: No PTR record found for {ip_address}.")
    except dns.resolver.Timeout:
        print(f"{bad}{Fore.RED} Error: The request timed out.")
    except dns.resolver.NoNameservers:
        print(f"{bad}{Fore.RED} Error: No nameservers available.")
    except dns.exception.DNSException as e:
        print(f"{bad}{Fore.RED} Error: {e}")
