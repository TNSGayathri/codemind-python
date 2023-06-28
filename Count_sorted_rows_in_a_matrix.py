a,b=map(int,input().split())
c=0
for i in range(a):
    l=list(map(int,input().split()))
    k=l[::-1]
    if(l==sorted(l)or k==sorted(k)):
        c+=1
print(c)