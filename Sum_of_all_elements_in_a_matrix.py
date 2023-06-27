a,b=map(int,input().split())
m=[]
s=0
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    s+=sum(l)
print(s)