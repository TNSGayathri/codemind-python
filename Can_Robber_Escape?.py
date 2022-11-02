n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(n):
    if(x[i]%2!=0):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")