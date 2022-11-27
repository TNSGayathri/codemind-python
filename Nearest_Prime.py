def ans(n):
    f=0
    for i in range(2,n//2+1):
        if(n%i==0):
            f=1
            break
    return f
n=int(input())
for i in range(n):
    a=int(input())
    for i in range(a,9999999):
        b=ans(i)
        if(b==0):
            c=i
            break
    for i in range(a,-1,-1):
        d=ans(i)
        if(d==0):
            e=i
            break
    f=abs(c-a)
    g=abs(e-a)
    if(f<g):
        print(c)
    else:
        print(e)
        