print("Hello! I am AI Bot. What's your name? :")
name = input()
print(f"Nice to meet you, " + name + "!")
print("How are you feeling today? (good/bad) : ")
mood = input().lower()
if mood == "good":
    print("That's great to hear! Keep up the positive vibes!")
elif mood == "bad":
    print("I'm sorry to hear that. Remember, after the rain comes the rainbow!")
else:
    print("I see! Thanks for sharing how you feel.")
print(f"It was nice chatting with you, {name}! Have a wonderful day!")
