n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    pre=[]
    x=0
    d={}
    for j in l:
        x+=j
        pre.append(x)
    for k in range(len(pre)):
        if pre[k]==b:
            print(1,k+1)
            break
        elif pre[k]-b in d:
            print(d[pre[k]-b]+2,k+1)
            break
        d[pre[i]]=i
    else:
        print(-1)