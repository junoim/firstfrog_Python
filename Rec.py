# def factorial_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#     pass
#
# number= int(input("Enter then number\n"))
#
# print(factorial_iterative(number))


# def factorial_recurssive(n):
#     if n ==1:
#         return 1
#     else:
#         return n* factorial_recurssive(n-1)
#
#
# number= int(input("Enter then number\n"))
#
# print(factorial_recurssive(number))

#fibonacci series:
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number= int(input("Enter then number\n"))

print(fibonacci(number))

