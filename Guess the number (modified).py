#Guess the Number game

print("One-Million-To-One")
print()
print()
counter = 0
while True:
  number = int(input("What is your guess?: "))
  if number == 1000000:
    print("CORRECT!")
    counter += 1
    break
  elif number < 1000000 and  number > 0:
    print("Too Low")
    counter += 1
  elif number > 1000000:
    print("Too High")
    counter += 1
  elif number < 0:
    print("I am Done! XP")
    exit()
  else:
    print("I can't process that")
  
print("It took you",counter,"guesses to get it correct!")
print("Thank you for using this program :)")
