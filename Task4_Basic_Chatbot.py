# ✅ TASK 4: Basic Chatbot

# Goal: Build a simple rule-based chatbot.
# Scope:
# ● Input from user like: "hello", "how are you", "bye".
# ● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!".
# Key Concepts Used: if-elif, functions, loops, input/output.

# ✅ TASK 4: Basic Chatbot

import re

def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()
        user_input = user_input.replace(" ", "")  # ✅ Remove all spaces

        # Simplified pattern match
        if re.search("hello|hi|hey", user_input):
            print("🤖 Chatbot: 👋 Hi there! How can I help you today?")
        elif "howareyou" in user_input:
            print("🤖 Chatbot: 😊 I'm doing great, thanks! What about you?")
        elif "yourname" in user_input:
            print("🤖 Chatbot: 🤖 I'm a simple chatbot created by you!")
        elif "thank" in user_input:
            print("🤖 Chatbot: 🙏 You're welcome!")
        elif user_input in ["bye", "exit", "goodbye"]:
            print("🤖 Chatbot: 👋 Goodbye! Have a great day!")
            break
        else:
            print("🤖 Chatbot: 🤔 I'm not sure how to respond to that.")

# Run the chatbot
chatbot()


