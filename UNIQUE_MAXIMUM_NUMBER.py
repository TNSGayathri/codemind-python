n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    c=1
    if(l[i]==-1):
        continue
    for j in range(len(l)):
        if(i!=j and l[i]==l[j]):
            c+=1
    if(c==1):
        k.append(l[i])
if(len(k)==0):
    print("-1")
else:
    print(max(k))