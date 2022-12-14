def fun(n):
    re=0
    temp=n
    while(n>0):
        r=n%10
        re=re*10+r
        n=n//10
    n1=temp+re
    t=n1
    res=0
    while(n1>0):
        k=n1%10
        res=res*10+k
        n1=n1//10
    if(t==res):
        return res
    else:
        return fun(t)
n=int(input())
print(fun(n))