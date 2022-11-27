import math
a,b=map(int,input().split())
s=int(math.log10(a)+1)
c=0
rev=0
c1=0
d=a//(10**(s-b))
while(c<b):
    r=a%10
    rev=rev*10+r
    c+=1
    a=a//10
while(rev>0):
    r=rev%10
    c1=c1*10+r
    rev=rev//10
print(abs(d-c1))