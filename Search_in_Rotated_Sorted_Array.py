n=int(input())
l1=list(map(int,input().split()))
a=int(input())
if a in l1:
    print(l1.index(a))
else:
    print(-1)