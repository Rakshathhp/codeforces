a=list(input("enter").split())
f={}
max_c=0
key=0
for i in a:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
    if f[i]>max_c:
        max_c=f[i]
        key=i
print(f)
print(key,max_c)





for j in f.values():
    print(j)
