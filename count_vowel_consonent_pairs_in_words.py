n=input().lower().split()
s="aeiou"
c="bcdfghjklmnpqrstvwxyz"
d=0
for i in n:
    j=0
    k=len(i)-1
    while j<k:
        if(i[j] in s and i[k] in c or i[j] in c and i[k] in s):
            d+=1
        j+=1
        k-=1
print(d)