n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(n):
    for j in range(i,n):
        s=sum(l[i:j+1:])
        m.append(s)
print(max(m))