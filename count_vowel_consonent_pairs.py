n=input().lower()
s="aeiou"
c="bcdfghjklmnpqrstvwxyz"
d=0
i=0
j=len(n)-1
while(i<j):
    if(n[i] in s and n[j]  in c or n[i]  in c and n[j] in s):
        d+=1
    i+=1
    j-=1
print(d)