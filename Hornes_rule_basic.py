import sys

def horn(t,k6=0,k5=0,k4=0,k3=0,k2=0,k1=0,k0=0):
    k5=t*k6+k5
    k4=t*k5+k4
    k3=t*k4+k3
    k2=t*k3+k2
    k1=t*k2+k1
    k0=t*k1+k0
    return k6,k5,k4,k3,k2,k1,k0
#

print("_ Hornes's rule _\r\n")
print("Please, enter integer coefficients for polynom, starting from 6 degree")
print("For example, for: ''3x^3 - 4x +5 =0''  would be: 0 0 0 3 0 -4 5\r\n")

k6 = int(raw_input("Please, enter coefficient of x^6: "))
k5 = int(raw_input("Please, enter coefficient of x^5: "))
k4 = int(raw_input("Please, enter coefficient of x^4: "))
k3 = int(raw_input("Please, enter coefficient of x^3: "))
k2 = int(raw_input("Please, enter coefficient of x^2: "))
k1 = int(raw_input("Please, enter coefficient of x^1: "))
k0 = int(raw_input("Please, enter coefficient of x^0 (free member): "))

t = int(raw_input("  Please, enter the integer root to test: "))
arr = horn(t,k6,k5,k4,k3,k2,k1,k0)

s=""
for Item in arr:
    s+=str(Item)+" "
print(s)

print("")
try:
    t = input("by_OlegTim. Press Enter key to quit")
except:
    sys.exit()
