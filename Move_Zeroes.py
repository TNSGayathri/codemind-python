n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if(l[j]==0):
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
for i in l:
    print(i,end=" ")