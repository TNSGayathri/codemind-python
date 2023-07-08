n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
for i in l:
    if i not in k:
        print(False)
        break
else:
    print("True")