n=input().lower()
for i in n:
    if(n.count(i)==1 and i.isalpha()):
        print(i)
        break
else:
    print("-1")