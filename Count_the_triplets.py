n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    c=0
    for j in range(a):
        for k in range(j+1,a):
            s=l[j]+l[k]
            if s in l:
                c+=1
    if(c==0):
        print("-1")
    else:
        print(c)