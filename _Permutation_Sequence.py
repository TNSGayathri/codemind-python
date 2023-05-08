import itertools as it
a,b=map(int,input().split())
l=[]
for i in range(1,a+1):
    l.append(i)
m=list(it.permutations(l))
c=list(m[b-1])
for i in c:
    print(i,end="")