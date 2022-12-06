n=input()
l=n.split()
for i in l:
    ma=ord(max(i))
    mi=ord(min(i))
    print(abs(ma-mi),end=" ")