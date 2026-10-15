n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    r=list(map(int,input().split()))
    j=max(r)
    h=j/2
    k=int(h)
    c=0
    if j==1:
        print(sum(r))
        continue
    
    
    for i in range(a):
        while r[i]>=k:
            r[i]-=k
            c+=1
    print(c)
    