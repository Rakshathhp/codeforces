from collections import Counter
n=int(input())
res=[]
f=0
for _ in range(n):
    a=input()
    for i in range(len(a)):
        if a[i]=='1':
            f=1
            res.append(i)
if f==0:
    print(0)
else:

    counter=Counter(res)

    print(max(counter.values()))