n=input()
d={}
for i in n:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
l=list(d.values())
c=l.count(max(l))
while(c>0):
    l.remove(max(l))
    c-=1
if(len(l)==0):
    print(-1)
else:
    for i in d:
        if d[i]==max(l):
            print(i)
            break