def res(n):
    fact=0
    for i in range(2,n//2+1):
        if(n%i==0):
            fact=1
            break
    return fact
n=int(input())
a=int(input())
for i in range(n,a+1):
    if(n==1):
        i+=1
    b=res(i)
    if(b==0):
        print(i)
    