def ans(n):
    f=0
    for i in range(2,n//2+1):
        if(n%i==0):
            f=1
            break
    return f
n=int(input())
for i in range(n,9999999):
    a=ans(i)
    if(a==0):
        c=i
        break
for i in range(n,-1,-1):
    b=ans(i)
    if(b==0):
        d=i
        break
e=abs(c-n)
f=abs(d-n)
if(e<=f):
    print(e)
else:
    print(f)