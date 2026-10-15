n=list(input("enter"))
r=[]
for i in n:
    if r:
        r.append(1)
    elif not r:
        for i in range(-1,0,-1):
            c=0
            if r[i]<r[-1]:
                c=c+1
            r.append(c)
print(r)
