t = int(input())

for _ in range(t):
    n = set()
    a, b = map(int, input().split())
    for i in range(a):
        x = input().lower()
        n.add(x[0])

    ok = True
    for j in range(b):
        y = input().lower()
        for ch in y:           
            if ch not in n:
                ok = False

    print("yes" if ok else "no")