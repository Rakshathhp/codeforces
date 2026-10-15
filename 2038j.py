
n=int(input("enter"))
left=0
for _ in range(n):
    i=input().split()
    a=i[0]
    c=int(i[1])
    if a=='p':
        left+=c
    elif a=='b':
        if c>left:
            print("yes")
            left=0    
        else:
            print("No")
            left-=c

