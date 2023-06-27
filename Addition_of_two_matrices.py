a=int(input())
m=[]
n=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(a):
    l=list(map(int,input().split()))
    n.append(l)
for i in range(a):
    for j in range(a):
        print(m[i][j]+n[i][j],end=" ")
    print()