a,b=map(int,input().split())
m=[]
s=0
r=[]
c=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    r.append(sum(l))
for i in range(b):
    s=0
    for j in range(a):
        s+=m[j][i]
    c.append(s)
if(max(r)>max(c)):
    print(max(r))
else:
    print(max(c))