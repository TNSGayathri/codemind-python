n=int(input())
for i in range(n):
    s=input()
    m=[]
    c=0
    for i in s:
        if i=='{' or i=="(" or i=="[":
            m.append(i)
        if c==1:
            break
        else:
            if i=='}':
                if len(m)!=0 and m[-1]=="{":
                    m.pop()
                else:
                    c=1
            if i==']':
                if len(m)!=0 and m[-1]=="[":
                    m.pop()
                else:
                    c=1
            if i==')':
                if len(m)!=0 and m[-1]=="(":
                    m.pop()
                else:
                    c=1
    if len(m)==0:
        print("True")
    else:
        print("False")
            
            