n=int(input())
l=list(map(int,input().split()))
x,y=0,0
for i in range(n):
    if i%2==0:
        x+=l[i]
    else:
        y+=l[i]
if abs(x-y)%4==0:
    print("X")
else:
    print("Y")