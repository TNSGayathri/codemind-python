import math
def ans(n):
    f=0
    if(n==1):
        f=1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            f=1
            break
    return f
n=int(input())
k=0
for i in range(2,n+1):
    if(ans(i)==0):
        if(n%i==0 and ans(n//i)==0):
            c=i
            d=n//i
            k+=1
if(k==0):
    print("-1")
else:
    print(d,c)
            