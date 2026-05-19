🤖 AI Chatbot (Python NLP Project)

🚀 Overview

The AI Chatbot is a beginner-friendly Python project that simulates a simple conversational assistant using predefined responses and user input matching.

The chatbot interacts with users through the terminal and responds to common messages such as greetings, questions, and exit commands.

This project demonstrates practical concepts of:

- Python logic building
- User interaction
- Conditional statements
- Basic Natural Language Processing (NLP)

---

🧠 Features

- Interactive command-line chatbot
- Responds to user messages
- Uses predefined conversational responses
- Runs continuously until user exits
- Beginner-friendly AI project

---

🛠️ Technologies Used

- Python

---

⚙️ Installation & Setup

1. Clone the repository or download files

---

2. Run the chatbot

python main.py

---

💻 Complete Code ("main.py")

responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing great!",
    "what is your name": "I am a Python AI Chatbot.",
    "bye": "Goodbye!"
}

print("🤖 AI Chatbot Started!")

while True:

    user = input("You: ").lower()

    if user in responses:
        print("Bot:", responses[user])

    else:
        print("Bot: I don't understand")

    if user == "bye":
        break

---

▶️ How It Works

1. User enters a message
2. Chatbot converts input into lowercase
3. Program checks if message exists in predefined responses
4. Matching response is displayed
5. Chat continues until user types:
bye
---

🎯 Skills Demonstrated

- Python Programming
- Conditional Logic
- Dictionaries in Python
- User Input Handling
- Basic AI Chatbot Concepts

---

🔮 Future Improvements

- Add more intelligent responses
- Use NLP libraries like NLTK
- Add voice recognition
- Create GUI version using Tkinter
- Build web version using Streamlit
- Integrate OpenAI API for advanced AI responses

---

👨‍💻 Author

Arsheen Shaikh

---
