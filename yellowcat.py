import os
import requests
import platform
from halo import Halo
import validators
from art import *
from termcolor import colored
from plugins.who_is import print_whois_info
from plugins.traceroute import print_traceroute_info
from plugins.dnslookup import print_dns_lookup_info
from plugins.reverse_dnslookup import print_reverse_dns_lookup_info
from plugins.geoip_lookup import print_geoip_lookup_info
from plugins.port_scan import print_port_scan_info
from plugins.page_links import print_page_links_info
from plugins.http_header import print_http_header_info
from plugins.email_header import print_email_header_info
from colorama import Fore, Style, init

version = "version 1.0.0"

def whois(params):
    print()
    print_whois_info(params)
    print()

def traceroute(params):
    print()
    print_traceroute_info(params)
    print()

def dnslookup(params):
    print()
    print_dns_lookup_info(params)
    print()
    
def reversedns(params):
    print()
    print_reverse_dns_lookup_info(params)
    print()

def geoip(params):
    print()
    print_geoip_lookup_info(params) 
    print()

def portscan(params):
    print()
    print_port_scan_info(params)
    print()

def pagelinks(params):
    print()
    print_page_links_info(params)
    print()

def httpheader(params):
    print()
    print_http_header_info(params)
    print()

def emailheader():
    print()
    print_email_header_info()
    print()
      
def print_menu():      
    print(colored("[01] Whois", "cyan"))
    print(colored("[02] Traceroute", "cyan"))
    print(colored("[03] DNS Lookup", "cyan"))
    print(colored("[04] Reverse DNS", "cyan"))
    print(colored("[05] GeoIP Lookup", "cyan"))
    print(colored("[06] Port Scan", "cyan"))
    print(colored("[07] Page Links", "cyan"))
    print(colored("[08] HTTP Header", "cyan"))
    print(colored("[09] Email Header", "cyan"))
    print(colored("[99] Exit", "cyan"))
    print()

def isIP(str):
    try:
        IP(str)
    except ValueError:
        return False
    return True

def main():
    loop = True
    while loop:
        # Check OS
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")

        cat_art = f'''
    |\__/,|   (`\\
  _.|o o  |_   ) )
-(((---(((-------- {Fore.GREEN}{version}
        '''

        # Print some badass ascii art header here !
        print(Fore.LIGHTYELLOW_EX + cat_art + Style.RESET_ALL)

        # Displays menu and choose options
        print_menu()    
        choice = input("Enter your choice [1-99]: ")
        if choice == "1":
            params = input("Enter IP or Domain for lookup: ")
            if validators.domain(params) or validators.ipv4(params):
                whois(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "2":
            params = input("Enter IP or Domain for lookup: ")
            if validators.domain(params) or validators.ipv4(params):
                traceroute(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "3":
            params = input("Enter Domain for lookup: ")
            if validators.domain(params):
                dnslookup(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "4":
            params = input("Enter IPv6 for lookup: ")
            if validators.ipv6(params):
                reversedns(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "5": 
            params = input("Enter IP for lookup: ")
            if validators.ipv4(params):
                geoip(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "6":
            params = input("Enter IP or Domain for lookup: ")
            if validators.domain(params) or validators.ipv4(params):
                portscan(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "7":
            params = input("Enter URL for lookup: ")
            if validators.url(params):
                pagelinks(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "8":
            params = input("Enter URL for lookup: ")
            if validators.url(params):
                httpheader(params)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "9":
            emailheader()
            input("Press [Enter] to continue...")
        elif choice == "99":
            loop=False
        else:
            print(colored("Wrong option selection. Enter any key to try again..", "red"))
        
if __name__ == "__main__":
    main()