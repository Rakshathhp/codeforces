n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    if x//2 < y:
        print("no")
    else:
        z=1
        for i in range(2,x):
                if x//i==y:
                    print("Yes")
                    z=1
                    break
                else:
                    z=0
        if z==0:
            print("no")
