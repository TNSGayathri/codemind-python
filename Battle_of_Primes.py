def ans(n):
    f=1
    if(n==1):
        f=0
    for i in range(2,n//2+1):
        if(n%i==0):
            f=0
            break
    return f
a=int(input())
b=int(input())
for i in range((a+b)+1,999999):
    if(ans(i)==1):
        print(i-(a+b))
        break