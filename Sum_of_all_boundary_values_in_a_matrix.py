a,b=map(int,input().split())
m=[]
s=0
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(a):
    for j in range(a):
        if(i == 0 or j == 0 or i == a- 1 or j == a- 1):
            s+=m[i][j]

print(s)
    