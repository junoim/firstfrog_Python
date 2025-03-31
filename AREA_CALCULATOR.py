import math

print("WELCOME TO AREA CALCULATOR!")
while True:
  print("Choose from the following shapes: ")
  print("(1)Square (2)Rectangle (3)Triangle (4)Circle")
  choice = int(input("Enter your choice :"))
  if choice == 1:
    print("you chose square!")
    side = float(input("Enter side in cm: "))
    area_square = side ** 2
    print(area_square)
  elif choice == 2:
    print("you chose Rectangle!")
    length = float(input("Enter length in cm: "))
    width = float(input("Enter width in cm: "))
    area_rectangle = length * width
    print(area_rectangle)
  elif choice == 3:
    print("you chose Triangle!")
    height = float(input("Enter height in cm: "))
    base = float(input("Enter base in cm: "))
    area_triangle = (height * base)/2
    print(area_triangle)
  elif choice == 4:
    print("you chose Circle!")
    radius = float(input("Enter radius in cm: "))
    area_circle = math.pi *(radius ** 2)
    print(area_circle)
  else:
    print("Invalid input")
  answer = input("Do you want to continue(y/n)? ")
  if answer == "y":
    continue
  else:
    print("THANK YOU FOR USING THE AREA CALCULATOR :)")
    break

