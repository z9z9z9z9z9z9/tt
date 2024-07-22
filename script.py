import asyncio
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    # Clear the screen (works on Unix and Windows)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

async def animate_text(text, delay=0.1):
    """ Animate text output. """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        await asyncio.sleep(delay)
    print()

async def main():
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + "Welcome to Command Central")
    print(Fore.GREEN + Style.BRIGHT + "=========================")
    
    # Async text animation
    await animate_text(Fore.GREEN + Style.BRIGHT + "TikTok Panel v2", 0.05)
    
    await asyncio.sleep(1)  # Brief pause after animation

    # Display available services
    services = [
        "1. Engagement Boost",
        "2. Followers Increase",
        "3. Likes Enhancement",
        "4. Comments Improvement",
        "5. Views Augmentation"
    ]

    print("\nAvailable Services:")
    for service in services:
        print(Fore.GREEN + service)
    
    url = input("\nEnter the source URL: ")
    
    try:
        service_choice = int(input("Choose a service by number: "))
        if service_choice < 1 or service_choice > 5:
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")
        return

    amount = input("Enter the amount (e.g., number of followers, likes, etc.): ")

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

    print(Fore.GREEN + "\nThank you for using Command Central. Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())
