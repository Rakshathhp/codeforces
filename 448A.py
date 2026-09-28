import math
a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=int(input())
c=sum(a)/5
d=sum(b)/10
cup=math.ceil(c)
med=math.ceil(d)
res=n-cup-med
if res>=0:
    print("yes")
else:
    print("No")





