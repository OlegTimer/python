import sys

warr=[]
parr=[]
print("_ NOTE THIS VERSION takes max mass disregarding the price (set it to 0) _\n")
print("_ 0-1 Knapsack Problem _\n")
print("Given integer and positive mass and price for items,") #in kg mass, in Newtons weight
print("what maximum value can you take, limited with knapsack mass capacity?")
print("(i.e. knapsack is 5 kg. Items: 2kg 2$; 3kg 4$: 4kg 5$. Max $ is 2+4$ for 2+3kg)")
print("Enter lines with mass TAB price to _input.txt in program's directory")
print("And run the program. (Items masses and prices are usually different).")
print("Items masses must be in non-decreasing order and not bigger than knapsack\n")

try:
    f = open('_input.txt')
except:
    f = open("_input.txt", "w")
    f.close()
else:
    f.close()

f = open("_input.txt", "r")
s = f.readline()
while( s ):
    d = s.split("\t")
    warr.append(int(d[0]))
    parr.append(int(d[1]))
    s = f.readline()
f.close()

if (len(warr)<1) or (len(parr)<1):
        try:
            t = input("Fill _input.txt. Press Enter key to quit")
        except:
            sys.exit()

print("Mass Price of items:")
for i in range (0,len(warr),1):
    s=str(warr[i])+"\t"+str(parr[i])
    print(s)

try:
    w = int(raw_input("\nEnter integer positive knapsack mass capacity, please: "))
except:
    sys.exit()
if w<1:
    sys.exit()

print("\nTotal mass inside.")
print("In columns headers: max_mass_capacity; in rows: mass for item:")
s="\t"
for i in range (0,w+1,1):
    s+=str(i)+"\t"
print(s)

arr= [[0 for i in range(w+1)] for i2 in range(len(warr))]

for i in range (0,w+1,1):
    if (i<warr[0]):
        arr[0][i]=0
    else:
        arr[0][i]=warr[0]

for i in range (1,len(warr),1):
    for i2 in range (1,w+1,1):
        if (i2<warr[i]):
            arr[i][i2]=arr[i-1][i2]
        else:
            if (arr[i-1][i2] > arr[i-1][i2-warr[i]]+warr[i]):
                arr[i][i2]=arr[i-1][i2]
            else:
                arr[i][i2]=arr[i-1][i2-warr[i]]+warr[i]

for i in range (0,len(warr),1):
    s=str(warr[i])+"\t"
    for i2 in range (0,w+1,1):
        s+=str(arr[i][i2])+"\t"
    print(s)

i= len(warr)-1
i2=w
print("\nMax mass is: "+str(arr[i][i2])+" kg")
while(max!=0):
    max=arr[i][i2]
    while(max==arr[i][i2] and i>-1):
        i-=1
    print("Take "+str(warr[i+1])+" kg")
    max-=warr[i+1]
    i2=max

try:
    t = input("\nby_OlegTim. Press Enter key to quit")
except:
    sys.exit()