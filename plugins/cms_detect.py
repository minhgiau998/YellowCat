import requests
from colorama import Fore, Style

def check_wordpress(url, html_content):
    """Checks for specific WordPress indicators"""
    if "/wp-content/" in html_content or "/wp-includes/" in html_content:
        return True

    # Check specific file
    try:
        res = requests.get(url + "/wp-login.php", timeout=5)
        if res.status_code == 200 and "user_login" in res.text:
            return True
    except:
        pass
    return False

def check_joomla(url, html_content):
    """Checks for specific Joomla indicators"""
    if "content=\"Joomla!" in html_content or "/templates/system/css/system.css" in html_content:
        return True

    try:
        res = requests.get(url + "/administrator/", timeout=5)
        if res.status_code == 200 and "Joomla" in res.text:
            return True
    except:
        pass
    return False

def check_drupal(url, html_content):
    """Checks for specific Drupal indicators"""
    if "Drupal" in html_content or "/sites/default/files" in html_content:
        return True

    try:
        res = requests.get(url + "/user/login", timeout=5)
        if res.status_code == 200 and "edit-name" in res.text:
            return True
    except:
        pass
    return False

def print_cms_info(url):
    """
    Main function to detect CMS
    """
    # URL normalization
    if not url.startswith("http"):
        url = "http://" + url
    url = url.rstrip("/")

    print(f"{Fore.BLUE}[~] Analyzing target for CMS signatures: {Fore.WHITE}{url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Get the Homepage content
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        html_content = response.text

        detected = []

        # Check WordPress
        if check_wordpress(url, html_content):
            detected.append("WordPress")
            print(f"{Fore.GREEN}[+] CMS Detected: WordPress")
            print(f"{Fore.CYAN}    -> Found common paths (/wp-content/) or login page.")

        # Check Joomla
        if check_joomla(url, html_content):
            detected.append("Joomla")
            print(f"{Fore.GREEN}[+] CMS Detected: Joomla")
            print(f"{Fore.CYAN}    -> Found Joomla meta tag or /administrator/ endpoint.")

        # Check Drupal
        if check_drupal(url, html_content):
            detected.append("Drupal")
            print(f"{Fore.GREEN}[+] CMS Detected: Drupal")
            print(f"{Fore.CYAN}    -> Found Drupal signatures in HTML.")

        # Summary
        if not detected:
            print(f"{Fore.YELLOW}[-] Could not detect a standard CMS (WordPress/Joomla/Drupal).")
            print(f"{Fore.WHITE}    The site might be custom-coded or using a modern JS framework (React/Vue/Angular).")

            # Bonus: Check for generator tag
            if "generator" in html_content.lower():
                for line in html_content.splitlines():
                    if "meta name=\"generator\"" in line.lower():
                        print(f"{Fore.MAGENTA}[!] Found Generator Meta Tag: {line.strip()}")

    except requests.exceptions.SSLError:
        print(f"{Fore.RED}[-] SSL Error. Try changing http/https.")
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}[-] Connection failed. Is the site up?")
    except Exception as e:
        print(f"{Fore.RED}[-] Error during CMS detection: {str(e)}")
