import mailparser
from colorama import init, Fore
from core.colors import info, que, bad, good, run, res

# Initialize colorama
init(autoreset=True)

def print_email_header_info():
    try:
        # Read raw email content from file
        with open("./db/raw_email.txt", "r") as file:
            raw_email = file.read().strip()  # Read and strip whitespace

        if not raw_email:
            print(f"{bad}{Fore.RED} Error: Empty raw email file.")
            return
        
        # Parse the raw email
        mail = mailparser.parse_from_string(raw_email)

        # Check if the parsing was successful
        if not mail.from_:
            print(f"{bad}{Fore.RED} Error: Failed to parse the raw email format.")
            return

        # Print the email headers
        print(f"{run}{Fore.WHITE} Email headers:")
        # Display email information
        print(f"{good}{Fore.LIGHTGREEN_EX} Attachments:")
        for attachment in mail.attachments:
            print(f"\t{good}{Fore.LIGHTGREEN_EX} {Fore.YELLOW}{attachment['filename']}")
        print(f"{good}{Fore.LIGHTGREEN_EX} Date: {Fore.YELLOW}{mail.date}")
        print(f"{good}{Fore.LIGHTGREEN_EX} Timezone: {Fore.YELLOW}{mail.timezone}")
        print(f"{good}{Fore.LIGHTGREEN_EX} To:")
        for to in mail.to:
            for t in to:
                print(f"\t{good}{Fore.YELLOW} {t}")
        print(f"{good}{Fore.LIGHTGREEN_EX} From:")
        for from_ in mail.from_:
            for f in from_:
                print(f"\t{good}{Fore.YELLOW} {f}")
        print(f"{good}{Fore.LIGHTGREEN_EX} Received:")
        for received in mail.received:
            for key, value in received.items():
                print(f"\t{good}{Fore.LIGHTGREEN_EX} {key}: {Fore.YELLOW}{value}")
        print(f"{good}{Fore.LIGHTGREEN_EX} Subject: {Fore.YELLOW}{mail.subject}")
        print(f"{good}{Fore.LIGHTGREEN_EX} Body:")
        for text in mail.text_plain:
            print(f"\t{Fore.YELLOW}{text}")

    except FileNotFoundError:
        print(f"{bad}{Fore.RED} Error: File './db/raw_email.txt' not found.")
    except IsADirectoryError:
        print(f"{bad}{Fore.RED} Error: './db/raw_email.txt' is a directory, not a file.")
    except Exception as e:
        print(f"{bad}{Fore.RED} An error occurred: {e}")
