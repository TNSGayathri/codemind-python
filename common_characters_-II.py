n=input().lower().split()
m=input().lower().split()
l=list(set("".join(n)))
k=list(set("".join(m)))
c=0
for i in l:
    if i in k:
        c+=1
print(c)