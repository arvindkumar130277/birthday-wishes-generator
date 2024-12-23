import json

# Function to get user input for the birthday message
def get_user_input():
    print("Welcome to the Birthday Wishes Generator!")
    
    name = input("Enter the name of the person: ").strip()
    relationship = input("Enter your relationship with the person (e.g., friend, family, partner): ").strip()
    special_message = input("Enter any special message or memory you'd like to include (optional): ").strip()
    
    return {
        "name": name,
        "relationship": relationship,
        "special_message": special_message
    }

# Function to generate a personalized birthday message
def generate_birthday_message(user_profile):
    base_message = f"Happy Birthday, {user_profile['name']}! 🎉\n"
    base_message += f"From your {user_profile['relationship']}, wishing you a wonderful day filled with love and joy! 🎂\n"
    
    if user_profile['special_message']:
        base_message += f"\nA special note: {user_profile['special_message']}"
    
    return base_message

# Function to save the birthday message to a text file
def save_birthday_message(message, name):
    file_name = f"birthday_wish_for_{name.replace(' ', '_').lower()}.txt"
    with open(file_name, "w") as file:
        file.write(message)
    print(f"Your birthday wish has been saved to {file_name}!")

# Main function to run the tool
def main():
    user_profile = get_user_input()
    birthday_message = generate_birthday_message(user_profile)
    
    print("\nYour Personalized Birthday Message:")
    print("-" * 50)
    print(birthday_message)
    print("-" * 50)
    
    save_choice = input("\nWould you like to save this message to a file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        save_birthday_message(birthday_message, user_profile['name'])

if __name__ == "__main__":
    main()
