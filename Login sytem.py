print("REPLIT LOGIN SYSTEM")
print()
print()
Name = 'Shradha'
password = '21pilots'

def login():
  while True:
    Name_user = input("what is your username?: ")
    password_user = input("What is your password?: ")
    if Name != Name_user or password != password_user:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue
    elif Name == Name_user and password == password_user:
      print("Welcome to Replit!")
      break
    else :
      print("invalid input")
  exit()

login()
