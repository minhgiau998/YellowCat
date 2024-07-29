import geoip2.database
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

# Path to the GeoLite2 database file
GEOIP_DB_PATH = 'db/GeoLite2-City.mmdb'

def print_geoip_lookup_info(ip_address):
    try:
        with geoip2.database.Reader(GEOIP_DB_PATH) as reader:
            response = reader.city(ip_address)
            print(f"{run}{Fore.WHITE} GeoIP lookup results for {ip_address}:")
            print(f"{good}{Fore.LIGHTGREEN_EX} Country: {Fore.YELLOW}{response.country.name}")
            print(f"{good}{Fore.LIGHTGREEN_EX} City: {Fore.YELLOW}{response.city.name}")
            print(f"{good}{Fore.LIGHTGREEN_EX} Latitude: {Fore.YELLOW}{response.location.latitude}")
            print(f"{good}{Fore.LIGHTGREEN_EX} Longitude: {Fore.YELLOW}{response.location.longitude}")
    except geoip2.errors.AddressNotFoundError:
        print(f"{bad}{Fore.RED} Error: Address {ip_address} not found in the GeoIP database.")
    except geoip2.errors.GeoIP2Error as e:
        print(f"{bad}{Fore.RED} Error: {e}")
