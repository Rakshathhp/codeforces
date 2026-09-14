n=int(input())
for _ in range(n):
    h=int(input())
    a=list(map(int,input().split()))
    r=[]
    for ch in a:
        if ch in r:
            pass
        else:
            r.append(ch)
    print(len(r))