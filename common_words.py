n=input().lower().split()
m=input().lower().split()
s=[]
for i in m:
    if i  in n and i not in s:
        s.append(i)
print(" ".join(s))

