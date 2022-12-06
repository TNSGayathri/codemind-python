n=input()
l=n.split()
ma=[]
mi=[]
for i in l:
    ma.append(ord(max(i)))
    mi.append(ord(min(i)))
print(abs(sum(ma)-sum(mi)))