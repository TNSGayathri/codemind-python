n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    if l[i]<0:
        l[i]=-1*l[i]
l.sort()
for i in range(len(l)):
    l[i]=l[i]*l[i]
    print(l[i],end=" ")