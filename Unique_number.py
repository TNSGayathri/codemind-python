n=int(input())
l=[]
while(n>0):
    r=n%10
    l.append(r)
    n=n//10
s=list(set(l))
if(len(s)==len(l)):
    print("Unique Number")
else:
    print("Not Unique Number")