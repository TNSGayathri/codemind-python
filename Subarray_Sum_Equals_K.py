a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i==b:
        c+=1
for i in range(0,a-1):
    if(l[i]+l[i+1]==b):
        c+=1
print(c)