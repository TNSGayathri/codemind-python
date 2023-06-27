a,b=map(int,input().split())
m=[]
l1=[]
l2=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    for j in l:
        if(j%2==0):
            l1.append(j)
        else:
            l2.append(j)
print(sum(l1),sum(l2))
        