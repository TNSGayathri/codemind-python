def square(n):
    res=1
    if(n==1):
        res=0
    else:
        for i in range(1,(n//2)+1):
            if(n==i*i):
                res=0
                break
    return res   
n=int(input())
x=list(map(int,input().split()))
s=0
for i in range(n):
    ans=square(x[i])
    if(ans==0):
        s=s+x[i]
print(s)
    