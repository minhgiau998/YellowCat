import requests
import concurrent.futures
import threading
import sys
from colorama import Fore, Style

# A global event flag to signal threads to stop
stop_event = threading.Event()

# A small built-in list for quick scans
DEFAULT_WORDLIST = [
    "admin", "login", "dashboard", "uploads", "images", "assets",
    "css", "js", "api", "backup", "secret", "config", "server-status",
    ".env", ".git", "wp-admin", "wp-content", "phpmyadmin", "robots.txt",
    "administrator", "site", "public", "private", "temp", "tmp",
    "test", "dev", "staging", "auth", "users", "passwords", "cpanel",
    "webmail", "logs", "cache", "db", "database"
]

def check_url(target_url, path):
    """
    Worker function to check a single path.
    Checks the stop_event before running to allow fast exit.
    """
    # 1. Check if we should stop
    if stop_event.is_set():
        return

    url = f"{target_url}/{path}"

    try:
        # User-agent to look like a browser
        headers = {'User-Agent': 'Mozilla/5.0 (YellowCat)'}

        # 2. Short timeout is crucial for responsiveness
        res = requests.get(url, headers=headers, timeout=3, allow_redirects=False)

        # 3. Double check stop event after request
        if stop_event.is_set():
            return

        status = res.status_code

        # Output logic
        if status == 200:
            print(f"\n{Fore.GREEN}[+] Found (200): {Fore.WHITE}/{path}")
        elif status in [301, 302]:
            print(f"\n{Fore.YELLOW}[>] Redirect ({status}): {Fore.WHITE}/{path}")
        elif status == 403:
            print(f"\n{Fore.MAGENTA}[!] Forbidden (403): {Fore.WHITE}/{path}")
        elif status == 500:
            # Sometimes errors are interesting
            pass

    except requests.RequestException:
        pass

def print_dir_fuzz_info(url):
    """
    Main function for Directory Fuzzing
    """
    # Reset the stop event in case it was set previously
    stop_event.clear()

    if not url.startswith("http"):
        url = "http://" + url
    url = url.rstrip("/")

    print(f"{Fore.BLUE}[~] Starting Directory Fuzzing on: {Fore.WHITE}{url}")
    print(f"{Fore.CYAN}[?] Enter path to wordlist file (Press Enter to use default list):")
    wordlist_path = input(f"{Fore.WHITE}Path: ").strip()

    words_to_scan = []

    if wordlist_path:
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                words_to_scan = [line.strip() for line in f if line.strip()]
            print(f"\n{Fore.BLUE}[INFO] Loaded {len(words_to_scan)} words.")
        except FileNotFoundError:
            print(f"\n{Fore.RED}[-] File not found. Using default list.")
            words_to_scan = DEFAULT_WORDLIST
    else:
        print(f"\n{Fore.BLUE}[INFO] Using built-in default list.")
        words_to_scan = DEFAULT_WORDLIST

    print(f"\n{Fore.YELLOW}[INFO] Starting scan with 20 threads... (Press Ctrl+C to stop)\n")

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
    futures = []

    try:
        # Submit all tasks
        for word in words_to_scan:
            if stop_event.is_set():
                break
            future = executor.submit(check_url, url, word)
            futures.append(future)

        # Wait for results and watch for KeyboardInterrupt
        for future in concurrent.futures.as_completed(futures):
            if stop_event.is_set():
                break
            try:
                future.result()
            except Exception:
                pass

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Interrupt detected! Stopping threads...")
        stop_event.set()  # Raise the red flag

        # Cancel any tasks that haven't started yet
        for f in futures:
            f.cancel()

        # Do NOT wait for threads to finish, kill the executor immediately
        executor.shutdown(wait=False)
        print(f"\n{Fore.RED}[!] Scan stopped.")
        return

    # Clean cleanup if scan finishes normally
    executor.shutdown(wait=True)
    print(f"\n{Fore.BLUE}[~] Scan complete.")
