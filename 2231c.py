t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    opp=0
    while len(set(a))>1:
        min_v=min(a)
        for i in range(n):
            if a[i]%2==0:
                if a[i]!=min_v:
                    a[i]=a[i]//2
                    opp+=1
                    break
            else:
                a[i]+=1
                opp+=1
                break
    print(opp)