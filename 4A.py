n=int(input())
if n>2:
    for i in range(n):
        if i%2==0:
            if (n-i)%2==0:
                print("YES")
                break
            else:
                print("NO")
                break
else:
    print("NO")