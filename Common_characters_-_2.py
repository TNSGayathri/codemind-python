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
    
print(len(l))