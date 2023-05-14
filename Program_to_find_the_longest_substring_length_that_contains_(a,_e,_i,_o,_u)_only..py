n=input()
c=0
l=[]
m="aeiou"
for i in n:
    if i in m:
        c+=1
    else:
        l.append(c)
        c=0
    l.append(c)
print(max(l))
    
    