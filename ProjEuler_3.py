a = 600851475143
i=1
c=1
m=[]
while i<=(a):
    if a%i==0:
        a=a/i
        for c in range(2,(i//2)+1):
            if i%c==0:
                break
        else:
            m.append(i)
    i+=1

print(m[-1])


