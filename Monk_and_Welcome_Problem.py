n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=[]
for i in range (len(l)):
    for j in range(len(l)):
        if(i==j):
            k.append(l[i]+m[j])
print(*k)