n=int(input())
for j in range(n):
    a,b,c,d=map(int,input().split())
    l=0
    x=a//b
    y=a//c
    z=a//(b+c)
    if(x+y-z>=d):
        print("Win")
    else:
        print("Lose")