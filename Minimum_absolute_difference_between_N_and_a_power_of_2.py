import math
def sqrt(n):
    f=0
    for i in range(2,n//2+1):
        if(int(math.pow(2,i))==n):
            f=1
            break
    return f
n=int(input())
for i in range(n,99999):
    if sqrt(i)==1:
        a=i
        break
for i in range(n,-1,-1):
    if sqrt(i)==1:
        b=i
        break
if((a-n)<(n-b)):
    print(a-n)
else:
    print(n-b)
            