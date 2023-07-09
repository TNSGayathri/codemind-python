def bin(n):
    s=""
    if n==0:
        s+="0"
    while n:
        if n%2==0:
            s+="0"
        else:
            s+="1"
        n=n//2
    return s[::-1]
n=int(input())
m=(2**n)-1
for i in range(m+1):
    s=bin(i)
    while(len(s)<n):
        s='0'+s
    print(s)
