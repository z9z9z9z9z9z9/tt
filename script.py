import sys

def display_services():
    services = [
        "1. Engagement Boost",
        "2. Followers Increase",
        "3. Likes Enhancement",
        "4. Comments Improvement",
        "5. Views Augmentation"
    ]
    print("\nAvailable Services:")
    for service in services:
        print(service)
    print()

def get_user_input():
    url = input("Enter the source URL: ")
    display_services()
    try:
        service_choice = int(input("Choose a service by number: "))
        if service_choice < 1 or service_choice > 5:
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    amount = input("Enter the amount (e.g., number of followers, likes, etc.): ")
    
    # Here you can add more validations as needed
    return url, service_choice, amount

def process_request(url, service_choice, amount):
    services = {
        1: "Engagement Boost",
        2: "Followers Increase",
        3: "Likes Enhancement",
        4: "Comments Improvement",
        5: "Views Augmentation"
    }
    service_name = services[service_choice]
    
    print("\nProcessing your request...")
    # Simulate processing time
    import time
    time.sleep(2)
    
    # Mock success message
    print(f"Successfully sent request to '{service_name}' for URL '{url}' with amount '{amount}'.")

def main():
    print("Welcome to Command Central")
    print("=========================")
    
    url, service_choice, amount = get_user_input()
    process_request(url, service_choice, amount)
    
    print("\nThank you for using Command Central. Goodbye!")

if __name__ == "__main__":
    main()
