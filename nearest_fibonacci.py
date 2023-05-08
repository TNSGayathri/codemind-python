def fib(n):
    t1=0
    t2=1
    t3=1
    while(t3<n):
        t1,t2=t2,t3
        t3=t1+t2
    return t3==n
n=int(input())
for i in range(n,9999999):
    if fib(i):
        a=i
        break
for i in range(n,-1,-1):
    if fib(i):
        b=i
        break
if((a-n)<(n-b)):
    print(a)
elif((a-n)==(n-b)):
    print(b,a)
else:
    print(b)
        