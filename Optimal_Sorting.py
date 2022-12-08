for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(sorted(l)==l):
        print("0")
    else:
        print(max(l)-min(l))