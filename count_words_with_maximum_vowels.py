n=input().lower().split()
s="aeiou"
m=[]
for i in n:
    c=0
    for j in range(len(i)):
        if(i[j] in s):
            c+=1
    m.append(c)
print(m.count(max(m)))