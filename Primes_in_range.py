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
m=int(input())
c=0
for i in range(n,m+1):
    if(ans(i)==0):
        c+=1
print(c)