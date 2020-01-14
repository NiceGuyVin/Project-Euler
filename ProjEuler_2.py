fib=1
a=[1,2]
i=0
while a[-1]<=4000000:
    a.append(a[i]+a[i+1])
    i+=1
sum=0
for i in range(len(a)):
    if(a[i]%2==0):
        sum=sum+a[i]
print(sum)

