n=int(input("enter n"))
for _ in range(n):
    a=list(map(int,input("enter list").split()))
    sum=0
    for i in range(len(a)):
        if i<6:
            sum-=a[i]
        else:
            sum+=a[i]
    print(sum)

