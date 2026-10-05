n = int(input())
a = list(map(int, input().split()))

mn = float('inf')
ans = (1, 2)

for i in range(n):
    j = (i + 1) % n
    d = abs(a[i] - a[j])

    if d < mn:
        mn = d
        ans = (i + 1, j + 1)

print(*ans)