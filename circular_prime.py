def ans(n):
    f=0
    for i in range(2,n//2+1):
        if(n%i==0):
            f=1
            break
    return f
n=int(input())
a=ans(n)
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
b=ans(rev)
if(a==0 and b==0):
    print("circular prime")
elif(a==1 and b==1):
    print("not prime")
else:
    print("prime but not a circular prime")