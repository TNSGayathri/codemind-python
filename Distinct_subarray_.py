def sub_array(l):
    s=[]
    m=[]
    for i in range(len(l)+1):
        for j in range(i+1,len(l)+1):
            s=l[i:j]
            m.append(s)
    return m
a=int(input())
b=int(input())
l=[i for i in range(a,b+1)]
m=sub_array(l)
c=0
for i in m:
    if sum(i)%2!=0:
        c+=1
print(c)