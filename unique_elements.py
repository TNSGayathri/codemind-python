n=int(input())
l=list(map(int,input().split()))
for i in range (len(l)):
    c=1
    if(l[i]==-1):
        continue
    for j in range(len(l)):
        if(i!=j and l[i]==l[j]):
            c+=1
            l[j]=-1
    print(l[i],end=" ")