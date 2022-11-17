#GUESS THE NUMBER
# 1. You are free to use anything we've studied till now.'
# 2. The number of guesses should be limited, i.e (5 or 9).
# 3. Print the number of guesses left.
# 4. Print the number of guesses he took to win the game.
# 5. “Game Over” message should display if the number of guesses becomes equal to 0.


n=21
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<21:
        print("you enter less number please input greater number.\n")
    elif guess_number>21:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")