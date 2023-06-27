a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    print(sum(l),end=" ")