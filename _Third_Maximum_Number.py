n=int(input())
l=list(map(int,input().split()))
m=list(set(l))
m.sort()
if(len(m)==1):
    print(m[0])
elif (len(m)==2):
    print(m[1])
else:
    print(m[len(m)-3])