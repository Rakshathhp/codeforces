a,b=map(int,input().split())
c=list(map(int,input().split()))
f=0
for i in range(len(c)):
    if c[i]>=b:
        f=1
if f==0:
    print("YES")
else:
    print("NO")
    