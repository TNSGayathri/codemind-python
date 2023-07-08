n=int(input())
l=list(map(int,input().split()))
m=[]
s=[]
for i in range(n-1,-1,-1):
    c=0
    if len(s)==0:
        m.append(-1)
        s.append(l[i])
    else:
        m.append(max(s))
        s.append(l[i])
print(*(m[::-1]))