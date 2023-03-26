a=int(input())
b=int(input())
c=0
l=[]
for i in range(a,b+1):
    if i %2==1:
        c+=1
    l.append(i)
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i]%2==0 and l[j]%2==1) or (l[i]%2==1 and l[j]%2==0):
            c+=1
print(c)