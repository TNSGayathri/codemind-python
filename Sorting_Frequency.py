n=int(input())
l=list(map(int,input().split()))
l=sorted(l)[::-1]
m=sorted(l,key=l.count)
d=[]
for i in m:
    if i not in d:
        d.append(i)
print(*(d[::-1]))