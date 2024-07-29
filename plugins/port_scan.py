import nmap
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_port_scan_info(target):
    try:
        nm = nmap.PortScanner()
        # Define Nmap options
        options = "-sS -sV -O -A -p 1-1000"
        nm.scan(target, arguments=options)  # Scan all ports from 1 to 65535 with aggressive timing
        print(f"{run}{Fore.WHITE} Starting nmap port scan on {target}:")
        
        for host in nm.all_hosts():
            print(f"{run}{Fore.WHITE} Host : {host} ({nm[host].hostname()})")
            print(f"{run}{Fore.WHITE} State : {Fore.GREEN if nm[host].state() == 'up' else Fore.RED}{nm[host].state()}")
            for proto in nm[host].all_protocols():
                print(f"{run}{Fore.WHITE}----------")
                print(f"{run}{Fore.WHITE} Protocol : {proto}")
                
                lport = nm[host][proto].keys()
                for port in lport:
                    print(f"{good}{Fore.LIGHTGREEN_EX} port : {port}\tstate : {Fore.YELLOW}{nm[host][proto][port]['state']}")
    except nmap.PortScannerError as e:
        print(f"{bad}{Fore.RED} Nmap scan error: {e}")
    except Exception as e:
        print(f"{bad}{Fore.RED} Error: {e}")
