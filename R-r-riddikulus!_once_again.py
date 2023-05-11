a,b=map(int,input().split())
l=list(map(int,input().split()))
m=[]
for i in range(b,len(l)):
    m.append(l[i])
for i in range(b):
    m.append(l[i])
print(*m)