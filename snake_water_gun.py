# Snake water gun
""" This is a two-player game where each player chooses one object. As we know, there are three objects, snake, water, and gun. So, the result will be
- Snake vs. Water: Snake drinks the water hence wins.
- Water vs. Gun: The gun will drown in water, hence a point for water
- Gun vs. Snake: Gun will kill the snake and win.
- In situations where both players choose the same object, the result will be a draw.
"""


# INSTRUCTIONS~
# - You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
# - You do not have to use a print statement in case of the above function.
# - Then you have to give input from your side.
# - After getting ten consecutive inputs, the computer will show the result based on each iteration.
# - You have to use loops (while loop is preferred).

import random
print("Welcome to the game of snake water gun,\nYou have 10 choices")

a = 0
b = 0
c = 0

while a < 11:
    q = input("what do you choose?\n")
    print(q)

    list = ["snake", "gun", "water"]
    choice = random.choice(list)

    if q == choice:
        print(" ohh it's a tie")
    elif (q == "snake" and choice == "water") or (q == "water" and choice == "gun") or (q == "gun" and choice == "snake"):
        print("Congratulation, you won!")
        b = b +1
    else:
        print("Oops, you lost!")
        c = c + 1

    a = a + 1

if b > c :
    print("you won", b, ":", c, "times")
elif b < c:
    print("you lost", b, ":", c, "times")
else:
    print("Its a tie", b, ":", c, "times")
