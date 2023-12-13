import sys

def issimple(var):
    counter=1
    sq = int (var**0.5)
    i=2
    while i<sq+1:
        counter+=1
        if var%i==0:
            break
        i+=1;
    if i>=sq+1:
        i=counter # yes var is simple
    else:
        i=-counter # no var is NOT simple
    return i
#
print("_ Eratosthenes method of finding simple nums_ \n")
try:
    n = int(raw_input("Enter max +num of int array (1...n}, please : "))
except:
    sys.exit()

if n<2:
    sys.exit()

print("\nCheck every int from 1 : ")
count=0
i=1
s=""
for i in range (1,n+1,1):
    d =  issimple(i)
    if d>0:
        s+=str(i)+" "
        count+=d
    else:
        count+=-d
print(s)
s="Iterations count is: " + str(count)
print(s)
s="Also you need to calculate square root of each "+str(n)+" nums."
print(s)

print("\nEratosthenes method:")
s=""
count=0
arr=[]
for i in range (1,n+1,1):
    arr.append(1)

k=1
while k*k<n:
    k+=1
    if arr[k]==1:
        i=k*k
        while i<n:
            count+=1
            arr[i]=0
            i=i+k

for i in range (1,n,1):
    if arr[i]==1:
        s+=str(i)+" "
print(s)
s="Iterations count is: " + str(count)
print(s)
s="Also you need to create array of each "+str(n)+" nums (faster than sq root)."
print(s)

print("")
try:
    t = input("by_OlegTim. Press Enter key to quit")
except:
    sys.exit()
