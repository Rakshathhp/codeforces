t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    c = 0

    if a[0] == 1:
        for i in range(1, n):
            if a[i] == 0:
                a[0], a[i] = a[i], a[0]
                c += 1
                break

    if a[n - 1] == 1:
        for i in range(n - 2, -1, -1):
            if a[i] == 0:
                a[n - 1], a[i] = a[i], a[n - 1]
                c += 1
                break

    if a[0] == 0 and a[n - 1] == 0:
        print(c)
    else:
        print(-1)