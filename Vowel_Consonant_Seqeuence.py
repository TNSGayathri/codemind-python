n=input()
s="aeiou"
m=[]
c=""
for i in n:
    if(i in s):
        m.append("V")
    else:
        m.append("C")
for i in range(len(m)-1):
    if(m[i]=="C" and m[i+1]=="C" or m[i]=="V" and m[i+1]=="V"):
        m[i]=0
for i in m:
    if(i!=0):
        c+=i
print(c)