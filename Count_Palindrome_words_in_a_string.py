n=input().lower()
l=n.split(" ")
c=0
for i in l:
    if(i==i[::-1]):
        c+=1
print(c)