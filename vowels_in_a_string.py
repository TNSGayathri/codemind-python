n=input()
a=input()
f=0
for i in range(len(n)):
    if(n[i]==a):
        f=1
        c=i
        break
if(f==1):
    print("True")
    print(c)
else:
    print("False")
        