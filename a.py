import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=input().split()
    arr.sort()
    f=[]
    b=[]
    for i,s in enumerate(arr):
        if i%2==0:
            f.append(s)
        else:
            b.append(s)
    b.reverse()
    print("".join(f+b))