import random

player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    print("Player 1 wins!")
elif player2_roll > player1_roll:
    print("Player 2 wins!")
else:
    print("It's a tie!")