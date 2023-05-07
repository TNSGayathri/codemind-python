n=int(input())
l=list(map(int,input().split()))
k=int(input())
m=[]
for i in range(0,n):
    if k==l[i]:
        m.append(i)
        break
for i in range(n-1,-1,-1):
    if k==l[i]:
        m.append(i)
        break
if len(m)==0:
    m=[-1,-1]
    print(*m)
else:
    print(*m)