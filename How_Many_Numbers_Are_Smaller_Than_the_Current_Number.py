n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(l[j]<l[i]):
            c+=1
    print(c,end=" ")