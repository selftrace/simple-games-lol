import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

selected_number = random.choice(numbers)
selected_suit = random.choice(suits)


print("Your card is:", selected_number, "of", selected_suit)
