import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_page_links_info(domain):
    try:
        response = requests.get(domain)
        if response.status_code != 200:
            print(f"{bad}{Fore.RED} Error: Unable to access {domain}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                links.add(href)
            elif href.startswith('/'):
                links.add(domain + href)

        print(f"{run}{Fore.WHITE} Links found on {domain}:")
        for idx, link in enumerate(links, start=1):
            print(f"{good}{Fore.LIGHTGREEN_EX} {Fore.YELLOW}{link}")
    
    except requests.exceptions.RequestException as e:
        print(f"{bad}{Fore.RED} Error: {e}")
