m=[]
op=[]
for a in range(100,1000):
    for b in range(100,1000):
        m.append(a*b)
m.sort()
cm=m[::-1]
cm_1=[str(item) for item in cm]
for i in range(len(cm_1)):
    if cm_1[i]==cm_1[i][::-1]:
        op.append(cm_1[i])
print(op[0])