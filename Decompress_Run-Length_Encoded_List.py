n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(1,len(l),2):
    c=0
    while c<l[i-1]:
        m.append(l[i])
        c+=1
print(*m)