"""
Animal Sound Generator
Concept: While loops only
"""

print("Animal Sounds Generator")
print()
print()
exit = " "
while exit != "yes":
  animal = input(("What animal do you want?:"))
  if animal == "Cow":
    print("MOOO")
  elif animal == "Dog":
    print("WOOF")
  elif animal == "Cat":
    print("MEOW")
  else:
    print("Ohhh,sorry we don't have that data :(")
  exit = input("Exit?:")
