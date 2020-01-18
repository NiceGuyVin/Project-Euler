import math as mt
m=[]
for i in range(2,200000):
    ct = 0
    for c in range(2,int(mt.sqrt(i))):
        if i%c == 0:
            ct = 1
            break
    if ct == 0:
        m.append(i)
print(m[10001])

