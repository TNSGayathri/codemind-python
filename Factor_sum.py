def fact(n):
    s=1
    for i in range(2,n+1):
        if(n%i==0):
            s+=i
    return s
l=list(map(int,input().split(",")))
m=[]
for i in l:
    if fact(i) in l:
        m.append(i)
m.sort()
if(len(m)!=0):
    print(*m)
else:
    print("-1")
