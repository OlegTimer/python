import sys
print("_ Multistage_rocket_calc_ \n")

m = float(raw_input("Enter cargo mass, please (in tonnes i.e. 20.1): "))
v = float(raw_input("Enter required delta-v (in km\s i.e. LEO with losses 9): "))
w = float(raw_input("Enter specific impulse (in km\s i.e. oxygen-hydrogen 4.5): "))
s = float(raw_input("Enter mass perfection (full/empty i.e. 15): "))
e = 2.71828

print("\nWith equal stages total launch mass will be:")

for n in range (1,10,1):
    st="for " +str(n)+" stage(s): "
    p=(e**(v/w)) * (((s-1)/(s-e**(v/(n*w))))**n)
    if (p<=0):
        st+=" not_possible"
    else:
        st+=str(p*m) + " t"
    print(st)

print("")
try:
    t = input("by_OlegTim. Press Enter key to quit")
except:
    sys.exit()