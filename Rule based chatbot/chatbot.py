print("Welcome to Rule Based Chatbot")
print("Type exit to quit")
responses={"hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey!",
    "how are you": "I am doing great!",
    "help": "Try: hello, hi, how are you, bye, exit",
    "bye": "Goodbye!"}
while True:
    user_input = input("\nYou: ")
    clean_input = user_input.lower().strip()
    if clean_input == "exit":
        print("Bot: Exiting chatbot...")
        break
    response = responses.get(
        clean_input,
        "Sorry, I don't understand that."
    )
    print("Bot:", response)