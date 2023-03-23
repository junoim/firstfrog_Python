#A pre-existing test file info.txt has some text written in it.Write a python
# function countvowel() that reads the contents of the file and counts the
# ocuurance of vowels (A,E,I,O,U) in the file
def countvowel():
    file = open("info.txt", "r")
    data = file.read()
    count = 0
    for i in data:
        if i == "AaEeIiOoUu":
            count += 1
        else:
            print("no vowels!")
    print ("total no. of vowels=",count)
    file.close()
countvowel()

#Write a function COUNT_AND() in Python to read text file "STORY.TXT"
# and count the number of times "AND" occurs in the file.
def COUNT_AND():
    file = open("story.txt", "r")
    data = file.read()
    count = 0
    for i in data :
        if i == "AND" or "and" or "And":
            count += 1
        else:
            print("ERROE!")
    print("total no. of AND/and/And = ",count)
    file.close()
COUNT_AND()

#Write a function countINDIA() which read a textfile 'myfile.txt'
# and print the frequency of the words 'India' in it(ignoring case of the word).
def countINDIA():
    file = open("myfile.txt","r")
    data = file.read()
    count = 0
    for i in data:
        if i == "INDIA" or "India":
            count += 1
        else:
            print("ERROR!")
    print("total no. of INDIA/India = ",count)
    file.close()
countINDIA()

#Write a function count Vowel() in Python,which should read each character of a text file "myfile.txt"and
# then count and display the count of occurance of vowels(including small cases and upper case)
def countVowel():
    file = open("myfile.txt", "r")
    data = file.read()
    count = 0
    for i in data:
        if i == "AaEeIiOoUu":
            count += 1
        else:
            print("no vowels!")
    print("total no. of vowels=", count)
    file.close()
countVowel()

#Write a method in python to read the content from a text file "Xyz.txt"
# line by line and display the same on the screen
file = open("Xyz.txt", "r")
data = file.readline()
for i in data:
    print(i,end="")
file.close()

#Write a method in python only those word whose length is 5.Display the same on the screen.
file = open("myfile.txt", "r")
data = file.read()
listdata = data.split()
for i in listdata :
    if len(i) == 5:
        print(i)
    else:
        print("not found")
file.close()

#Write a user-defined function to perform the following operations:
#Push the values into the stack if the price of products is greater than 100
#Pop and display the contents of the stack
product = {'Book': 250,'Pen':120, 'Pencil':50, 'Notebook' : 400, 'Register':480}
st=[]
def PUSH(Values):
    st.append(Values)

def POP():
    return st.pop()

for i, in product.items():
    if product[i] >100:
        PUSH(product[i])
print(st)

while True:
    if st!=[]:
        print(POP())
    else:
        break
#Create a stack after checking the elements if it is even then multiply by 2
# and if the element is odd,then multiply it by 3.
#Pop and display the contents of the stack
list =[2,3,4,5,6,7,8,9,10]
st=[]
def PUSH(list):
    st.append(list)
def POP():
    return st.pop()
for [i] in list:
    if [i]/2 == 0 :
        PUSH([i]*2)
    else:
        PUSH([i]*3)
print(st)
while True:
    if st!=[]:
        print(POP())
    else:
        break

#Push the keys(name of Department)of the dictionary into a stack,
# where the corresponding value (Number of PC) is 25 or more.
#Pop and display the content of the stack
SETUP={"HR":10, "QUALITY":25,"SUPPORT":50, "PRODUCTION":20, "SUPPLY":25}
st=[]
def PUSH():
    st.append()
def POP():
    return st.pop()
for i in SETUP.items():
    if product[i] >= 25:
        PUSH([i])
    else:
        print("don't know that!")
print(st)
while True:
    if st !=[]:
        print(POP())
    else:
        break

#Traverse the content of the list and push the numbers into a
# stack which are divisible by 3
#Pop and display the content of the stack.
N=[3,5,10,13,21,23,45,56,60,78]
st=[]
def PUSH(values):
    st.append(values)
def POP():
    return st.pop()
for [i] in N:
    if i%3 == 0 :
        PUSH([i])
    else:
        print("ERROR!")
print(st)
while True:
    if st != []:
        print(POP())
    else:
        break

#Push the keys(name of the student) of the dictionary into a stack,
# where the corresponding value(marks) are more than 79
#Pop and display the content of the stack
R={"RAKESH":70,"OMESH":50,"VISHWAS":70,"ANITA":80,"ANUSHRI":90}
st=[]
def PUSH(values):
    st.append(values)
def POP():
    return st.pop()
for i in R.keys():
    if R.keys[i] > 79:
        PUSH([i])
    else:
        print("ERROR!")
print(st)
while True:
    if st != []:
        print(POP())
    else:
        break

#Traverse the content of the list and push the numbers higher than 33 into a stack
#Pop and display the content of the stack.
def PUSH(values):
    st.append(values)
def POP():
    return st.pop()
st=[]
N=[12,13,34,56,21,79,98,22,35,38]
for [i] in N:
    if i>33:
        PUSH([i])
    else:
        print("ERROR!")
print(st)
while True:
    if st!=[]:
        print(POP())
    else:
        break

#Write a function ETCount() in python,which should read each character of
# text file "TEXTFILE.TXT" and count and display the count of
# occurance of aplhabets E and T indivually (including small cases e and t too)
def ETCount():
    file = open("TESTFILE.txt", "r")
    data = file.read()
    count = 0
    for i in data:
        if i =="ETet":
            count += 1
        else:
            print("not working on that")
    print("occurance of E & T = ",count)
ETCount()

#Write a function INDEX_LIST(L),where L is the list elements passed as
# argument to the function.The function returns another list
# named 'indexlist' that stores the indices of all Non-Zero Elements of L

def INDEX_LIST(L):
    indexlist=[]
    for i in range(len(L)):
        if L[i]!=0:
            indexlist.append(i)
    return indexlist

L = [12,4,0,11,0,56]
print(INDEX_LIST(L))

#stack name status
#Push_element()- To push an object containing name and Phone number
# of customers who live in Goa to the stack
#Pop_element()- To pop the objects from the stack and display them
# .Also display "stack empty" when they are no elements in the stack.
stacks=[]
def PUSH():
    stacks.append():
def POP():
    return stacks.pop()
L1 = ["Gurdas","9999999999","Goa"]
L2 = ["Julee","8888888888","Mumbai"]
L3 = ["Murugan","7777777777","Cochin"]
L4 = ["Ashmit","1010101010","Goa"]
for i in L1:
    if i[2] == "Goa":
        print(i[0] and i[1])
    else:
        print("not found")
for i in L2:
    if i[2] == "Goa":
        print(i[0] and i[1])
    else:
        print("not found")
for i in L3:
    if i[2] == "Goa":
        print(i[0] and i[1])
    else:
        print("not found")
for i in L4:
    if i[2] == "Goa":
        print(i[0] and i[1])
    else:
        print("not found")
while True:
    if stacks !=[]:
        print(POP())
    else:
        print("Stack Empty")

#Write a method in python to read lines from a text file"xyz.txt"
# and display those lines which are starting with an alphabet "o"
file = open("xyz.txt", "r")
data = file.readline()
datalist = data.split()
for i in datalist():
    if i[0] == "Oo":
        print(i,end" ")
    else:
        print("no o")

















































