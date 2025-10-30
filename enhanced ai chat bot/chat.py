def enhanced_chatbot():
    print("Hello! I'm your AI Chatbot 😊")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

    while True:
        mood = input("How are you feeling today? (good/bad/neutral): ").lower()
        if mood == "good":
            print("That's awesome! Keep smiling 😄")
        elif mood == "bad":
            print("Oh no! I'm here for you. Want to talk about what happened?")
        elif mood == "neutral":
            print("Got it! Hope your day becomes more exciting soon!")
        else:
            print("Hmm, I didn't get that. Let's try again!")

        hobby = input("What do you like to do for fun? ")
        print(f"Wow, {hobby} sounds really interesting!")

        fav_food = input("What's your favorite food? ")
        print(f"Yum! I also love {fav_food}!")

        cont = input("Would you like to continue chatting? (yes/no): ").lower()
        if cont == "no":
            print(f"It was nice chatting with you, {name}! Have a great day! 👋")
            break

enhanced_chatbot()
