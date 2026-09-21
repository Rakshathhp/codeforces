t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n % 2:
        n -= k
        ans = 1
    else:
        ans = 0

    ans += (n + (k - 2)) // (k - 1)

    print(ans)