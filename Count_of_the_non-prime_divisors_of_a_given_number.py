def res(n):
    fact=0
    d=0
    for i in range(2,n//2+1):
        if(n==1):
            fact=1
            break
        elif(n%i==0):
            fact=1
            break
    if(fact==1):
        d=1
    return d
n=int(input())
c=1
for i in range(1,n+1):
    if(n%i==0):
        a=res(i)
        if(a==1):
            c+=1
print(c)
        