import math
def bi(n):
    s=""
    if n==0:
        s+='0'
    while n:
        if(n%2==0):
            s+="0"
        else:
            s+="1"
        n=n//2
    if len(s)<3:
        while(len(s)<3):
            s+="0"
    return s[::-1]
n=int(input())
s=[]
while n>0:
    r=n%(10)
    s.append(r)
    n=n//(10)
s=s[::-1]
m=[]
for i in s:
    m.append(bi(i))
m="".join(m)
m=list(map(int,m))
n=m.index(1)
l=m[n::]
for i in l:
    print(i,end="")