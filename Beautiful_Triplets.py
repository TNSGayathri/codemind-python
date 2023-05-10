n=int(input())
l=list(map(int,input().split()))
m=[n]
while(len(l)>=1):
    c=l.count(min(l))
    for i in range(c):
        l.remove(min(l))
    m.append(len(l))
m.remove(0)
for i in m:
    print(i)