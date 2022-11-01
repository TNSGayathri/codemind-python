n=int(input())
x=list(map(int,input().split()))
for i in range(n-1,(n//2)-1,-1):
    print(x[i],end=" ")
for i in range(n//2):
    print(x[i],end=" ")
    