def res(n):
    rev=0
    temp=n
    e=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(rev==temp):
        print(rev,end=" ")
a=int(input())
b=int(input())
d=0
for i in range(a,b+1):
    d=res(i)
