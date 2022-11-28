n=int(input())
l=list(map(int,input().split()))
ma=0
c1=-999
for i in range(len(l)):
    c=1
    if(l[i]==-1):
        continue
    for j in range(len(l)):
        if(i!=j and l[i]==l[j]):
            c+=1
            l[j]=-1
    if(c1<c):
        c1=c
        ma=l[i]
    elif(c1==c):
        c1=c
        ma=min(ma,l[i])
print(ma)