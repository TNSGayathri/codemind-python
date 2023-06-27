a,b=map(int,input().split())
m=[]
s=0
k=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(b):
    s=0
    for j in range(a):
        s+=m[j][i]
    k.append(s)
print(*k)    