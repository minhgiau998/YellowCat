from icmplib import traceroute, ICMPError
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_traceroute_info(destination):
    last_distance = 0
    print(f"{'Distance/TTL':<15} {'Address':<15} {'Average round-trip time'}")
    try:
        packet = traceroute(destination)
        for ttl in packet:
            if last_distance + 1 != ttl.distance:
                print(Fore.RED + f"{'*':<15} {'Some gateways are not responding':<25}")
            print(Fore.GREEN + f'{ttl.distance:<15} {ttl.address:<25} {ttl.avg_rtt:.3f} ms')
            last_distance = ttl.distance
    except ICMPError as e:
        print(f"[{Fore.GREEN}+{Fore.RESET}] {e}")
