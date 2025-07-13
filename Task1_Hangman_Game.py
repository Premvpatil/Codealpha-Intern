# ✅ TASK 1: Hangman Game

# Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
# Simplified Scope:
# ● Use a small list of 5 predefined words (no need to use a file or API).
# ● Limit incorrect guesses to 6.
# ● Basic console input/output — no graphics or audio.
# Key Concepts Used: random, while loop, if-else, strings, lists.

import random

# Predefined list of words
words = ["apple", "tiger", "robot", "house", "plant"]
word = random.choice(words)

guesses = []
attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "

    print(display.strip())

    if "_" not in display:
        print("🎉 You won! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("⚠️ Already guessed.")
        continue

    guesses.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"❌ Wrong guess. Attempts left: {attempts}")

if attempts == 0:
    print("💀 You lost! The word was:", word)
