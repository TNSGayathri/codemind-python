import math
n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    if(i<0):
        i=abs(i)
    if(i!=0):
        d=int(math.log10(i)+1)
        m.append(d)
    
    else:
        m.append(1)
        
print(*m)
        