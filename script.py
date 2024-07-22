import asyncio
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    # Clear the screen (works on Unix and Windows)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

async def animate_text(text, delay=0.05):
    """ Animate text output. """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        await asyncio.sleep(delay)
    print()

async def display_header():
    clear_screen()
    header = (
        Fore.GREEN + Style.BRIGHT +
        "==============================\n" +
        "  _______ _   _ _____ _  \n" +
        " |__   __| \\ | |_   _| | \n" +
        "    | |  |  \\| | | | | | \n" +
        "    | |  | . ` | | | | | \n" +
        "    | |  | |\\  |_| |_|_| \n" +
        "    |_|  |_| \\_|_____|(_)\n" +
        "                           \n" +
        "  _______ _  __  _______  \n" +
        " |__   __| |/ / |__   __| \n" +
        "    | |  | ' /     | |    \n" +
        "    | |  |  <      | |    \n" +
        "    | |  | . \\     | |    \n" +
        "    |_|  |_|\\_\\    |_|    \n" +
        "                           \n" +
        "==============================\n"
    )
    await animate_text(header, 0.03)

async def main():
    await display_header()
    
    # Display available services
    services = [
        "1. Engagement Boost",
        "2. Followers Increase",
        "3. Likes Enhancement",
        "4. Comments Improvement",
        "5. Views Augmentation"
    ]

    print(Fore.GREEN + "Available Services:")
    for service in services:
        print(Fore.GREEN + service)
    
    url = input(Fore.GREEN + "\nEnter the source URL: ")
    
    try:
        service_choice = int(input(Fore.GREEN + "Choose a service by number: "))
        if service_choice < 1 or service_choice > 5:
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
        return

    amount = input(Fore.GREEN + "Enter the amount (e.g., number of followers, likes, etc.): ")

    # Process request
    services_dict = {
        1: "Engagement Boost",
        2: "Followers Increase",
        3: "Likes Enhancement",
        4: "Comments Improvement",
        5: "Views Augmentation"
    }
    service_name = services_dict[service_choice]
    
    print(Fore.GREEN + "\nProcessing your request...")
    await asyncio.sleep(2)  # Simulate processing time

    print(Fore.GREEN + f"Successfully sent request to '{service_name}' for URL '{url}' with amount '{amount}'.")

    print(Fore.GREEN + "\nThank you for using TikTok Panel v20. Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())
