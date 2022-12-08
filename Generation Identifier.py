Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# Generation Identifier
print("Generation Identifier")
print()
print()
age = int(input("Which year were you born in?: "))
print()
if age >= 1925 and age <=1946:
  print("You are a traditionalist!")
elif age >= 1947 and age <= 1964:
  print("BABY BOOMERS!")
elif age >= 1965 and age <= 1981:
  print("you are from Generation X!cool!")
elif age >= 1982 and age <= 1995:
  print("Hah! Millenials. Enjoying your starbucks?")
elif age >= 1996 and age <= 2015:
  print("Woo!GenerationZ! going for the future huh?")
else:
  print("well I guess you are either the latest or should be back a the museum XD!")