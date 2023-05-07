n=int(input())
l=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if l[i]<=k<=l2[i]:
        c+=1
print(c)