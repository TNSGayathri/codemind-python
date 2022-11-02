n=int(input())
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if(b<n or c<n ):
        print("UPLOAD ANOTHER")
    else:
        if(b==c):
            print("ACCEPTED")
        else:
            print("CROP IT")
    