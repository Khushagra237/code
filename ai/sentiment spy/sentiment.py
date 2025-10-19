import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN}Welcome to Sentiment Spy! Analyze the sentiment of your text inputs easily.{Style.RESET_ALL}")
user_name = input(f"{Fore.YELLOW}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"
conversation_history = []
while True:
    user_input = input(f"{Fore.GREEN}> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Goodbye,! Stay positive!{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"{Fore.RED}Exiting Sentiment spy. Farewell, Agent {user_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.MAGENTA}Conversation history cleared. Starting fresh!{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.BLUE}No conversation history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, 1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                elif sentiment_type == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW
                print(f"{idx}. {color}{text}"
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color} {sentiment_type} sentiment detected!" 
            f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")
