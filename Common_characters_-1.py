n=input().lower().split()
f=0
for i in n[0]:
    for j in n:
        if i not in j:
            break
    else:
        print(i,end="")
        f=1
if f==0:
    print(-1)