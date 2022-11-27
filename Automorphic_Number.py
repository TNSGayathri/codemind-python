import math
n=int(input())
sq=n**2
d=int(math.log10(n)+1)
if(n==int(sq%(10**d))):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")