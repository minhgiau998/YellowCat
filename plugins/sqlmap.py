import subprocess
import sys
import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Define colors
info = f"{Fore.YELLOW}[INFO]"
que = f"{Fore.CYAN}[?]"
bad = f"{Fore.RED}[-]"
good = f"{Fore.GREEN}[+]"
run = f"{Fore.BLUE}[~]"
res = f"{Fore.MAGENTA}[>]"

def get_sqlmap_exe():
    """
    Get the absolute path to the sqlmap executable in the venv.
    """
    # 1. Determine where 'Scripts' (Windows) or 'bin' (Linux) is
    if sys.platform == "win32":
        scripts_dir = os.path.join(sys.prefix, 'Scripts')
        exe_name = 'sqlmap.exe'
    else:
        scripts_dir = os.path.join(sys.prefix, 'bin')
        exe_name = 'sqlmap'

    # 2. Construct the full path
    target_path = os.path.join(scripts_dir, exe_name)

    # 3. Verify it exists
    if os.path.isfile(target_path):
        return target_path

    return None

def check_sqlmap_installed():
    """Check if sqlmap executable runs correctly"""
    exe_path = get_sqlmap_exe()
    if not exe_path:
        return False

    try:
        # We run the executable with stdin=subprocess.DEVNULL to prevent timeouts
        result = subprocess.run(
            [exe_path, '--version'],
            capture_output=True,
            text=True,
            timeout=10,
            stdin=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def print_sqlmap_info(url):
    """Run SQLMap scan on the provided URL"""

    exe_path = get_sqlmap_exe()

    if not exe_path or not check_sqlmap_installed():
        print(f"\n{bad}{Fore.RED} Error: SQLMap executable not found or not working.")
        print(f"{info}{Fore.YELLOW} Diagnostic showed sqlmap.exe exists, but it might be corrupt.")
        print(f"{info}{Fore.YELLOW} Try reinstalling: pip uninstall sqlmap -y && pip install sqlmap")
        return

    print(f"\n{run}{Fore.WHITE} Starting SQLMap scan on: {url}")

    # SQLMap options menu
    print(f"{que}{Fore.CYAN} Select scan type:")
    print(f"{Fore.CYAN} [1] Basic scan (detect SQL injection)")
    print(f"{Fore.CYAN} [2] Full scan (detect + enumerate databases)")
    print(f"{Fore.CYAN} [3] Aggressive scan (all techniques)")
    print(f"{Fore.CYAN} [4] Custom options")

    scan_choice = input(f"{que}{Fore.WHITE} Enter your choice [1-4]: ").strip()

    # Base command using the absolute path to the executable
    base_cmd = [exe_path, '-u', url, '--batch']

    # Build command based on choice
    if scan_choice == "1":
        cmd = base_cmd + ['--smart', '--level=1', '--risk=1']
        print(f"{run}{Fore.WHITE} Running basic SQL injection detection...")
    elif scan_choice == "2":
        cmd = base_cmd + ['--dbs', '--level=2', '--risk=1']
        print(f"{run}{Fore.WHITE} Running full scan with database enumeration...")
    elif scan_choice == "3":
        cmd = base_cmd + ['--level=5', '--risk=3', '--dbs']
        print(f"{run}{Fore.WHITE} Running aggressive scan...")
    elif scan_choice == "4":
        custom_opts = input(f"{que}{Fore.WHITE} Enter custom options: ").strip()
        cmd = base_cmd + custom_opts.split()
    else:
        print(f"{bad}{Fore.RED} Invalid choice. Using basic scan.")
        cmd = base_cmd + ['--smart', '--level=1', '--risk=1']

    try:
        print(f"\n{run}{Fore.WHITE} Executing scan...\n")

        # KEY FIX: stdin=subprocess.DEVNULL prevents the hanging/timeout
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            stdin=subprocess.DEVNULL
        )

        for line in process.stdout:
            line = line.strip()
            if line:
                if 'vulnerable' in line.lower() or 'injectable' in line.lower():
                    print(f"{good}{Fore.LIGHTGREEN_EX} {line}")
                elif 'error' in line.lower() or 'failed' in line.lower():
                    print(f"{bad}{Fore.RED} {line}")
                elif 'testing' in line.lower() or 'checking' in line.lower():
                    print(f"{run}{Fore.LIGHTBLUE_EX} {line}")
                elif 'database' in line.lower():
                    print(f"{res}{Fore.LIGHTYELLOW_EX} {line}")
                else:
                    print(f"{Fore.WHITE} {line}")

        process.wait()

        if process.returncode != 0:
            err = process.stderr.read()
            # Only show error if it's not empty and not just warnings
            if err and "error" in err.lower():
                print(f"\n{bad} SQLMap stderr: {err}")
            else:
                print(f"\n{good}{Fore.LIGHTGREEN_EX} Scan completed.")
        else:
            print(f"\n{good}{Fore.LIGHTGREEN_EX} Scan completed successfully.")

    except KeyboardInterrupt:
        print(f"\n{bad}{Fore.YELLOW} Scan interrupted by user.")
    except Exception as e:
        print(f"{bad}{Fore.RED} Error running SQLMap: {str(e)}")
