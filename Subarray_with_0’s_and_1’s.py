n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(n):
    for j in range(i+1,n):
        l1=l[i:j+1]
        if(l1.count(0)==l1.count(1)):
            k=len(l1)
            if(m<k):
                a=i
                b=j
                m=k
if m==0:
    print(-1)
else:
    print(a,b)