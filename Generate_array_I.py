n=int(input())
l=list(map(int,input().split()))
i=0
m=[]
while i<len(l)-1:
    for j in range(l[i+1]):
        m.append(l[i])
    i+=2
print(*m)