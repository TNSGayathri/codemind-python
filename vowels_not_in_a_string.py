n=input()
n.lower()
l=['a','e','i','o','u']
k=[]
for i in n:
    if(i in l):
        l.remove(i)
if(len(l)==0):
    print("0")
else:
    print(*l)