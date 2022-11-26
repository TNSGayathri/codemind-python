import math
n=int(input())
f=0
x=len(str(n))-1
while(n):
    r=n//(10**x)
    if(r==6 and f==0):
        r=9
        f=1
    print(r,end="");
    n%=(10**x)
    x-=1