n=input().lower()
m=list(set(n))
if(" " in m):
    print(len(m)-1)
else:
    print(len(m))