n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in range(len(l)):
        for j in range(i,len(l)):
            s=0
            for k in range(i,j+1):
                s+=l[k]
            if(s==b and c==0):
                print(i+1,j+1)
                c+=1
                
    if(c==0):
        print("-1")
    