n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    while c<b:
        m=l[-1]
        l.remove(m)
        l.insert(0,m)
        c+=1
    print(*l)