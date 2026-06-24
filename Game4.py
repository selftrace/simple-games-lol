import random

words = ["python", "computer", "security", "network"]
secret_word = random.choice(words)
guess = input("Guess a letter: ")

display = ""

for letter in secret_word:
    if letter == guess:
        display = display + letter + " "
    else:
        display = display + "_ "

print(display)