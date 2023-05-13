n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
m=[]
for i in l1:
    if i not in l2:
        m.append(i)
for i in l2:
    if i not in l1:
        m.append(i)
print(*m)