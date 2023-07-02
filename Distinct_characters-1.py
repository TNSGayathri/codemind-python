n=input().lower()
s=""
for i in n:
    if(n.count(i)==1  and i.isalpha()):
        s+=i
print("".join(sorted(s)))