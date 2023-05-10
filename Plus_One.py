n=int(input())
l=list(map(int,input().split()))
d=""
m=[]
for i in l:
    d+=str(i)
c=int("".join(d))+1
while(c>0):
    r=c%10
    m.append(r)
    c=c//10
for i in range(len(m)-1,-1,-1):
    print(m[i],end=" ")