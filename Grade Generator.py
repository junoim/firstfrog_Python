#Grade Generator

print("Exam Grade Calculator")
print()
print()
Name = input("Name of exam: ")
Score = int(input("Max.Possible Score: "))
your_score = float(input("Your score: "))
percentage = your_score/Score * 100
if percentage >= 90 :
  print("You got",percentage,"% which is A+!","\033[32m","congratulations")
elif percentage >= 80 and percentage <= 90:
    print("You got",percentage,"% which is A!","\033[36m","congratulations")
elif percentage >= 70 and percentage <= 79:
    print("You got",percentage,"% which is B!","\033[33m","YAY")
elif percentage >= 60 and percentage <= 69:
    print("You got",percentage,"% which is C!","\033[34m","Don't worry!keep learning!everything will fall back to place.")
elif percentage >= 50 and percentage <= 59:
    print("You got",percentage,"% which is D!","\033[35m","Don't worry!keep learning!everything will fall back to place.")
elif percentage <= 50:
    print("You got",percentage,"% which is U!","\033[31m","Don't worry!The Harder you fall the higher you rise!Keep improving!.")
else:
  print("invalid input")
