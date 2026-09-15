n=int(input())
for _ in range(n):
    a=int(input())
    if a>=4:
        b=a//4
        c=a%4
        d=c//2
        print(b+d)
    else:
        b=a//2
        print(b)
   