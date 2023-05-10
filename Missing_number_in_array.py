n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    m=[]
    for i in range(1,a+1):
        m.append(i)
    for j in m:
        if j not in l:
            print(j)
            break