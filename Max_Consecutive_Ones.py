n=int(input())
l=list(map(int,input().split()))
c=0
m=[]
for i in l:
    if i==1:
        c+=1
    else:
        m.append(c)
        c=0
m.append(c)
print(max(m))