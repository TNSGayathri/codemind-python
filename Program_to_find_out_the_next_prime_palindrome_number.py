def  ans(n):
    f=0
    for i in range(2,n//2+1):
        if(n%i==0):
            f=1
            break
    return f
def res(n):
    rev=0
    t=n
    f=1
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(t==rev):
        f=0
    return f
n=int(input())
for i in range(n+1,9999999):
    f=ans(i)
    e=res(i)
    if(f==0 and e==0):
        print(i)
        break