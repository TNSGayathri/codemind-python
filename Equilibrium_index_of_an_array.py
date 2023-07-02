n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    for i in range(a):
        l1=l[:i-1:]
        l2=l[i::]
        if(sum(l1)==sum(l2)):
            print(i-1)
            break
    else:
        print(-1)