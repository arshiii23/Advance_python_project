responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing great!",
    "bye": "Goodbye!"
}

print("AI Chatbot Started!")

while True:

    user = input("You: ").lower()

    if user in responses:
        print("Bot:", responses[user])

    else:
        print("Bot: I don't understand")

    if user == "bye":
        break