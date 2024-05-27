'''a,b,c,d=map(int,input().split(" "))
if a-c<b-d:
    print("BUY FIRST TV")
elif a-c>b-d:
    print("BUY SECOND TV")
else:
    print("ANY")'''


a,b,c,d=map(int,input().split(" "))
fa=a-a*c/100
fb=b-b*d/100
if fa<fb:
    print("FIRST")
elif fa>fb:
    print("SECOND")
else:
    print("ANY")
