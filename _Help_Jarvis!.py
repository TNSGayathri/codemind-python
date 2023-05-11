n=int(input())
for i in range(n):
    a=int(input())
    l=[]
    while(a>0):
        r=a%10
        l.append(r)
        a=a//10
    l.sort()
    m=[i for i in range(min(l),max(l)+1)]
    m.sort()
    if(l==m):
        print("YES")
    else:
        print("NO")