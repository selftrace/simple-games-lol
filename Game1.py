import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

all_chars = letters + numbers + symbols

length = 8
password = ""

for i in range(length):
    random_char = random.choice(all_chars)
    password = password + random_char

print("Your password:", password)