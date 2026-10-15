n=int(input("enter n"))
for _ in range(n):
    m=int(input("emter n of list"))
    a=list(map(int,input("enter list").split()))
    x,y=0,len(a)
    mid=x//y
    z=""
    p=0
    while len(a)>0:
        a.pop(a[mid:])
        p+=1
print(p)