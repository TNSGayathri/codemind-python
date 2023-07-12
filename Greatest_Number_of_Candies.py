n=int(input())
l=list(map(int,input().split()))
a=int(input())
m=max(l)
s=[]
for i in l:
    if(i+a >= m):
        s.append("True")
    else:
        s.append("False")
print(*s)