n=int(input())
res=0
while(n>0):
    r=n%10
    res+=r*r
    n=n//10
    if(n==0 and res>9):
        n=res
        res=0
if(res==1 ):
    print("True")
else:
    print("False")