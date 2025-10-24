import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives",  "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["New York", "Paris", "Tokyo"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why do Java developers wear glasses? Because they don't see sharp.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why did the computer go to the doctor? Because it had a virus!"
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains or cities?")
    preference = input(Fore.YELLOW + "You :")
    preference = normalize_input(preference) 

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: I recommend you visit {suggestion}!")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You :").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Great! Enjoy your trip to {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Sorry to hear that. Let's try again.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again")
            recommend()
    else:
        print(Fore.RED + "TravelBot: I don't have that type of destination")

    Show_Help()
def pcking_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You :"))
    print(Fore.GREEN + f"TravelBot: How many days?")
    days = input(Fore.YELLOW + "You :")\
    
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days im {location}:")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring chargers/adapters")
    print(Fore.GREEN + "- Check the weather forecast")
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def Show_Help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (type: recommend)")
    print(Fore.GREEN + "- Provide packing tips (type: packing tips)")
    print(Fore.GREEN + "- Tell you a travel joke (type: tell me a joke)")
    print(Fore.CYAN + "- Exit (type: exit)\n")

def chat():
    print(Fore.CYAN + "Welcome to TravelBot! Your personal assistant.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    Show_Help()

    while True:
        user_input = input(Fore.YELLOW + f"{name} :")
        user_input = normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "packing tips" in user_input or "pack" in user_input:
            pcking_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "exit" in user_input or "quit" in user_input:
            print(Fore.CYAN + f"TravelBot: Goodbye, {name}! Safe travels!")
            break
        else:
            print(Fore.RED + "TravelBot: I didn't understand that. Please try again.")
        
if __name__ == "__main__":
    chat()