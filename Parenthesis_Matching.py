s=input()
m=[]
c,f=0,0
for i in range(len(s)):
    if s[i]=='{' or s[i]=='[' or s[i]=='(':
        m.append(s[i])
    if f==1:
        break
    else:
        if s[i]=='}':
            if len(m)!=0 and m[-1]=='{':
                m.pop()
            else:
                print(i+1)
                f=1
                break
        elif s[i]==']':
            if len(m)!=0 and m[-1]=='[':
                m.pop()
            else:
                print(i+1)
                f=1
                break
        elif s[i]==')':
            if len(m)!=0 and m[-1]=='(':
                m.pop()
            else:
                print(i+1)
                f=1
                break
if(f==0):
    if len(m)==0:
        print(0)
    else:
        print(len(s)+1)