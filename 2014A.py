n=int(input("enter n"))
for _ in range(n):
    a,b=map(int,input("enter a b").split())
    c=list(map(int,input().split()))
    grab=0
    res=0
    for i in range(a):
        if c[i]>1:
            grab=c[i]
        elif c[i]==0 and grab>0:
            grab-=1
            res+=1
    print(res)