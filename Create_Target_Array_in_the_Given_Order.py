n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
t=[]
for i in range(n):
    t.insert(k[i],l[i])
print(*t)
    