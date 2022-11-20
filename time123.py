import time
initial = time.time()

k=0
while(k<<45):
    print("this is shradha.")
    time.sleep(2)
    k+=1
print("while loop runs in",time.time()-initial,"seconds")

initial2 = time.time()
for i in range (45):
    print("this is harry")
print("For loop runs in",time.time()-initial2,"seconds")

localtime = time.asctime((time.localtime(time.time())))
print(localtime)