import requests
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_http_header_info(url):
    try:
        response = requests.get(url)
        print(f"{run}{Fore.WHITE} HTTP header lookup results for {url}:")
        for header, value in response.headers.items():
            print(f"{good}{Fore.LIGHTGREEN_EX} {header}: {value}")
    except requests.exceptions.MissingSchema:
        print(f"{bad}{Fore.RED} Error: {url} is not a valid URL.")
    except requests.exceptions.ConnectionError:
        print(f"{bad}{Fore.RED} Error: Failed to establish a connection to {url}.")
    except requests.exceptions.Timeout:
        print(f"{bad}{Fore.RED} Error: The request to {url} timed out.")
    except requests.exceptions.RequestException as e:
        print(f"{bad}{Fore.RED} Error: {e}")
