#Affirmation Generator

print("Wholesome positivity Machine")
print()
name = input("Who are you?\n")
print()
goal = input("What do you want to achieve?\n")
print()
a = 5
if name == "shradha" or name == "shreya":
  print("Hi",name,"!How u doin?")
  scale = input("On a scale of 1 -10 how do you feel today?\n")
  if scale >= str(a) :
    print("I am so happy for you",name,"!.Keep up the good work!")
  elif scale <= str(a) :
    print("hey",name,"keep your chin up!Today you're going to teach peopl to code in the most amazing way,simply by being you- YOU ROCK!")
  else :
    print("invalid input!")
