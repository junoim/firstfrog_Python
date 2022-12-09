#Fill in the blank Lyrics!

print("Fill in the blank Lyrics!")
print("type in the blank lyrics,see if you're as cool as me")
print()
print()
counter = 0
exit = ""
while exit != "give":
  exit = input("Never gonna ____ you up! ")
  if exit != "give":
    print("Nope,try again")
  else:
    print("Never gonna let you down!")
  counter += 1
print("well done, it took you",counter,"attempts!")
