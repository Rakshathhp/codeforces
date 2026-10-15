c=input("enter").split()
g={}
for w in c:
    a=list(w)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    key="".join(a)
    if key not in g:
        g[key]=[]
    g[key].append(w)
print(list(g.values()))
