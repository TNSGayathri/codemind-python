a,b=map(int,input().split())
s=0
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    s+=sum(l)
print(s)
    