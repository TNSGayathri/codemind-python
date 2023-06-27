a,b=map(int,input().split())
m=[]
s,s1=0,0
for i in range(a):
    l=list(map(int,input().split()))
    s+=sum(l)
    m.append(l)
for i in range(a):
    for j in range(b):
        if(i==0 or j==0 or j==b-1 or i==a-1):
            s1+=m[i][j]
print(s-s1)