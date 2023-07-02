n=input().lower()
m=list(set(n))
if(" " in m):
    m.remove(" ")
print("".join(sorted(m)))