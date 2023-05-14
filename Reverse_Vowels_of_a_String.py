a=input()
n=list(a)
l="aeiouAEIOU"
i=0
j=len(n)-1
while(i<j):
    if(n[i] in l and n[j] in l):
        n[i],n[j]=n[j],n[i]
        i+=1
        j-=1
    elif(n[i] in l):
        j-=1
    else:
        i+=1
s=""
for i in n:
    s+=str(i)
print(s)