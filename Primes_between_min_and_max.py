def prime(n):
    f=0
    if(n==1):
        f=1
    for i in range(2,n//2+1):
        if(n%i==0 ):
            f=1
            break
    return f
n=int(input())
l=list(map(int,input().split()))
m=l.index(min(l))
ma=l.index(max(l))
c=0
if(m<ma):
    s=l[m:ma+1:]
    for i in s:
        if prime(i)==0:
            c+=1
    print(c)
else:
    s=l[ma:m+1:]
    for i in s:
        if(prime(i)==0):
            c+=1
    print(c)