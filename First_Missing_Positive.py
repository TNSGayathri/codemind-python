n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(1,max(l)+2):
    m.append(i)
for i in m:
    if i not in l:
        print(i)
        break