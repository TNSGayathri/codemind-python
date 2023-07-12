n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    k=[]
    for i in l:
        k.append(i)
    l.sort()
    if k==l:
        print('0')
    else:
        print(max(k)-min(k))
    