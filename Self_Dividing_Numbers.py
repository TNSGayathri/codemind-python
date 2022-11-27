import math
def ans(n):
    t2=n
    c1=len(str(n))
    c2=0
    while(t2>0):
        r=t2%10
        if(r==0):
            t2=t2//10
            continue
        if(n%r==0):
            c2+=1
        t2=t2//10
    if(c1==c2):
        print(n,end=" ")
n=int(input())
m=int(input())
for i in range(n,m+1):
    ans(i)