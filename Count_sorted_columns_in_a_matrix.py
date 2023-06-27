a,b=map(int,input().split())
m=[]
c=0
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(b):
    k=[]
    for j in range(a):
        k.append(m[j][i])
    g=sorted(k)
    if(k==g):
        c+=1
print(c)
        