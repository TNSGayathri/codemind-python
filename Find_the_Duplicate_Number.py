n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    c=1
    if(a[i]==-1):
        continue
    for j in range(0,n):
        if(a[j]==a[i]  and i!=j):
            c+=1
    if(c>1):
        print(a[i])
        break