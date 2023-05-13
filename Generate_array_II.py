n=int(input())
l=list(map(int,input().split()))
m=[]
i=0
while i<len(l)-1:
    for j in range(l[i+1]):
        m.append(l[i])
    i+=2
print(*m)