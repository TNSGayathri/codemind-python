n=input().lower().split()
s="aeiou"
c=0
for i in n:
    if(i[0] in s and i[-1] not in s):
        c+=1
print(c)