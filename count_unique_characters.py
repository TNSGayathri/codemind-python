n=input().lower()
c=0
for i in n:
    if(n.count(i)==1 and i.isalpha()):
        c+=1
print(c)