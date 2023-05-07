def prime(n):
    f=0
    for i in range(2,n//2+1):
        if(n%i==0 or n==1):
            f=1
            break
    return f
n=int(input())
l=list(map(int,input().split()))
np,p=1,1
for i in l:
    if prime(i)==0:
        p=p*i
    else:
        np=np*i
print(abs(p-np))       