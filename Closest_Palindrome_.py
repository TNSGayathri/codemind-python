def res(n):
    f=0
    rev=0
    t=n
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(t==rev):
        f+=1
    return f
         
n=int(input())
for i in range(n+1,99999):
    a=res(i)
    if(a==1):
        c=i
        break
for i in range(n-1,-1,-1):
    b=res(i)
    if(b==1):
        d=i
        break
e=abs(c-n)
f=abs(d-n)
if(e==f):
    print(d,c)
elif(e<f):
    print(c)
else:
    print(d)