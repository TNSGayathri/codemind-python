def fact(a):
    s=1
    for i in range(2,a+1):
        if(a%i==0):
            s+=i
    return s
lst=list(map(int,input().split(",")))
l=[]
for i in lst:
    if fact(i) in lst:
        l.append(i)
if len(l)!=0:
    print(*l)
else:
    print("-1")