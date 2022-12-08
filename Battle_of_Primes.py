def ans(n):
    f=0
    if(n==1):
        f=1
    for i in range(2,n//2+1):
        if(n%i==0):
            f=1
            break
    return f
n=int(input())
m=int(input())
for i in range((n+m)+1,999999):
    if(ans(i)==0):
        print(abs((n+m)-i))
        break