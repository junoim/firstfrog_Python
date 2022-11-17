# Health Management System
# 3 clients - Harry, Rohan and Hammad
# Health Management System
# 3 clients - Harry, Rohan and Hammad

# def getdate():
#     import datetime
#     return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client






def getdate():
    import datetime
    return datetime.datetime.now()
def log(a):
    name= str(input("What is the client's name?:\n"))
    a= str(input("What do you want to log- Diet or Exercise:\n"))
    x= 'diet'
    y = 'exercise'
    z = 'Rohan'
    m = 'Harry'
    n=  'Hammad'
    if a == x:
       l= print(str(input("ok,whose diet do you want to log into?:\n")))
       if l==m:
           def getdate():
            file=open("Harry_diet.txt",'w')
            file.write(str(input()))
            file.close()
       if l==n:
           def getdate():
            file=open("Hammad_diet.txt",'w')
            file.write(str(input()))
            file.close()
       if l==z:
           def getdate():
            file=open("Rohan_diet.txt",'w')
            file.write(str(input()))
            file.close()

    if a == y:
       l= print(str(input("ok,whose exercise do you want to log into?:\n")))
       if l==m:
           def getdate():
            file=open("Harry_exercise.txt",'w')
            file.write(str(input()))
            file.close()
       if l==n:
           def getdate():
            file=open("Hammad_exercise.txt",'w')
            file.write(str(input()))
            file.close()
       if l==z:
           def getdate():
            file=open("Rohan_exercise.txt",'w')
            file.write(str(input()))
            file.close()


def retrieve(a):
        name = str(input("What is the client's name?:\n"))
        b = str(input("What do you want to retrieve- Diet or Exercise:\n"))
        x = 'diet'
        y = 'exercise'
        z = 'Rohan'
        m = 'Harry'
        n = 'Hammad'
        if b == x:
            l = print(str(input("ok,whose diet do you want to retrieve into?:\n")))
            if l == m:
                def getdate():
                    file = open("Harry_diet.txt", 'r+')
                    file.read()
                    file.close()
            if l == n:
                def getdate():
                    file = open("Hammad_diet.txt", 'r+')
                    file.read()
                    file.close()
            if l == z:
                def getdate():
                    file = open("Rohan_diet.txt", 'r+')
                    file.read()
                    file.close()

        if b == y:
            l = print(str(input("ok,whose exercise do you want to retrieve ?:\n")))
            if l == m:
                def getdate():
                    file = open("Harry_exercise.txt", 'r+')
                    file.read()
                    file.close()
            if l == n:
                def getdate():
                    file = open("Hammad_exercise.txt", 'r+')
                    file.read()
                    file.close()
            if l == z:
                def getdate():
                    file = open("Rohan_exercise.txt", 'r+')
                    file.read()
                    file.close()


question = str(input("What do you want to use this program for? login or retrieve data?:\n"))
s = 'login'
p = 'retrieve'
print(question)
if question == s:
  print(log(a))
if question == p:
  print(retrieve())

print("Thank you for using this program")