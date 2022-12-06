n=input()
l="aeiouAEIOU"
k=[]
for i in n:
    if i in l and i not in k:
        k.append(i)
if(len(k)==0):
    print("-1")
else:
    print(*k)