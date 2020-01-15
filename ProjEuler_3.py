a = 600851475143
i=1
m=[]
while i<=(a):
    if a%i==0:
        a=a/i
        m.append(i)
    i+=1

print(m[-1])

