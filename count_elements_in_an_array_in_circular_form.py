n=int(input())
x=list(map(int,input().split()))

x.append(x[0])
x.append(x[1])
c=0
for i in range(n):
    if (x[i]%2==0 and x[i+2]%2!=0) or (x[i]%2!=0 and x[i+2]%2==0 ):
        c+=1
print(c)