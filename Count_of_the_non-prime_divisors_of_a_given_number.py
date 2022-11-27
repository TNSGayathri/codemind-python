def ans(n):
    f=0
    for i in range(2,n//2+1):
        if(n%i==0):
            f=1
            break
    return f
n=int(input())
c=1
for i in range(2,n+1):
    if(n%i==0):
        a=ans(i)
        if(a==1):
            c+=1
print(c)          