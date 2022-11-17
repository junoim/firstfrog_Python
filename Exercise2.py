#FAULTY CALCULATOR

# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result


print("Enter your first number:")
num1 = int(input())
print("Enter your second number:")
num2 = int(input())
num3 = {'+', '*', '-', '/', '%'}
print('so What you Want?'+'+,-,/,%,*')
num3 = input()
if num1 == 45 and num2 == 3 and num3 == '*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '+':
    num4 = num1 + num2
    print(num4)
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '-':
    num4 = num1 - num2
    print(num4)
elif num3 == '/':
    num4 = num1 / num2
    print(num4)
elif num3 == '%':
    num4 = num1 % num2

else:
    print("invalid input!")





