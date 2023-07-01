n=input().lower()
s="abcdefghijklmnopqrstuvwxyz0123456789 "
c=0
for i in n:
    if i not in s:
        c+=1
print(c)