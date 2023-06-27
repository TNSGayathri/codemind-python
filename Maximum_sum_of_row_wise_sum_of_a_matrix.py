a,b=map(int,input().split())
m=[]
s=0
k=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    k.append(sum(l))
print(max(k))