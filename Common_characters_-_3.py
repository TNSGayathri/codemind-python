n=input().lower().split()
f=0
l=[]
for i in n[0]:
    for j in n:
        if i not in j:
            break
    else:
        l.append(i)
        f=1
if f==0:
    print(-1)
else:
    print(min(l))