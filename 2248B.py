t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < 2 * m:
        print("NO")
        continue

    a.sort()
    b.sort()

    ok = True

    for i in range(m):
        if a[i] >= b[i]:
            ok = False
            break

    if not ok:
        print("NO")
        continue

    j = m

    for x in b:
        while j < n and a[j] <= x:
            j += 1

        if j == n:
            ok = False
            break

        j += 1

    print("YES" if ok else "NO")