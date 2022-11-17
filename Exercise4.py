# - You have to take an integer type variable, and the input of the variable will define the length of the triangle.
# - You have to declare another Boolean variable.
# - When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
# - But if the value of Boolean is 0 or false, then the triangle will be printed upside down.



x=int(input("Enter the number of rows you want to print:\n"))
a=int(input("Enter 1 for True and 0 for False\n"))
if(a==0):
    for i in range(2,x+1):
        for j in range(i):
            print("*",end="")
        print()
elif(a==1):
    for i in range(2,x+1):
        for j in range(x-i):
            print("*",end="")
        print()
elif(a==7):
    for i in range(5,x+5):
        for j in range(i):
            print("#",end="")
print()






