t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    total = 0
    ans = 0

    for i in range(n):
        word = input()

        if total + len(word) <= m:
            total += len(word)
            ans += 1
        else:
            for _ in range(i + 1, n):
                input()
            break

    print(ans)