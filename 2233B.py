t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    if n % 2 == 0:
        for i in range(1, n + 1, 2):
            x = i
            y = i + 1
            ans += [y, x, x, y, x, y, y, x]

    else:
        ans += [3, 3, 2, 1, 1, 2, 1, 2, 2, 3, 1, 3]

        for i in range(4, n + 1, 2):
            x = i
            y = i + 1
            ans += [y, x, x, y, x, y, y, x]

    print(*ans)