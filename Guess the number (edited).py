import random
print("Totally Random One-Million-to-One")
print()
print()
attempt = 0
while True :
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  myNumber = random.randint(1,100)
  if user_guess < myNumber:
    print("too low")
    attempt += 1
  elif user_guess > myNumber:
    print("too high")
    attempt += 1
    continue
  elif user_guess == myNumber:
    print("You are a winner! 🥳🥳")
    break
    exit()
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
