n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    for j in range(a):
        l1=l[:j:]
        l2=l[j+1::]
        if sum(l1)==sum(l2):
            print("YES")
            break
    else:
        print("NO")