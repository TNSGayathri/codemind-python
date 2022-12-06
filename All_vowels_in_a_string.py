n=input()
n.lower()
a=set(n)
c=0
l="aeiou"
for i in a:
    if(i in l):
        c+=1
        
if(c==5):
    print("True")
else:
    print("False")