import random

treasure = {
    "row": random.randint(1, 5),
    "col": random.randint(1, 5)
}

found = False

while found == False:
    print("\n--- New Guess ---")
    user_row = int(input("Enter row (1-5): "))
    user_col = int(input("Enter column (1-5): "))

    if user_row == treasure["row"] and user_col == treasure["col"]:
        print("You found the treasure!")
        found = True
    else:
        print("Nothing here... Try again!")