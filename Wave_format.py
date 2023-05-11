n=int(input())
l=list(map(int,input().split()))
l.sort()
x=1
a=[]
b=[]
for i in range(n-1,-1,-1):
    if(x==1):
        a.append(max(l))
        l.remove(max(l))
        x=0
    else:
        b.append(max(l))
        l.remove(max(l))
        x=1
if(len(a)==len(b)):
    for i in range(len(a)):
        print(b[i],a[i],end=" ")
else:
    c=min(len(a),len(b))
    for i in range(c):
        print(b[i],a[i],end=" ")
    if(c==len(a)):
        print(b[c],end="")
    else:
        print(a[c],end="")