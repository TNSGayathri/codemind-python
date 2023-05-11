def sub_array(l,a):
    s=[]
    m=[]
    for i in range(0,a+1):
        for j in range(i+1,len(l)+1):
            s=l[i:j]
            m.append(s)
    return m
c=0    
a,b=map(int,input().split())
l=list(map(int,input().split()))
m=sub_array(l,a)
for i in m:
    if sum(i)==b:
        c+=1
print(c)