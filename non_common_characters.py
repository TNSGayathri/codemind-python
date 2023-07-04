n=input().lower().split()
m=input().lower().split()
n="".join(n)
m="".join(m)
s=[]
for i in n:
    if i not in m  and i not in s:
        s.append(i)
for i in m:
    if i not in n and i not in s:
        s.append(i)
s=sorted(s)
print("".join(s))

        