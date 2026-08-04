n=int(input())
for _ in range(n):
    a=list(map(int,input().strip()))
    if 1 in a:
        a.remove(1)
    if 0 in a:
        a.remove(0)
    print(*a,sep="")