def lcm(a,b):
    i=1
    while 1:
        m=b*i
        if m%a==0:
            return m
        i+=1
    
n=int(input())
l=list(map(int,input().split()))
m=1
for i in l:
    m=lcm(m,i)
print(m)
    