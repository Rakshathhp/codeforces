import sys
input = sys.stdin.readline

def find(parent, a):
    root = a
    while parent[root] != root:
        root = parent[root]
    # path compression: point everyone along the way directly to root
    while parent[a] != root:
        parent[a], a = root, parent[a]
    return root

def union(parent, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra != rb:
        parent[ra] = rb

t = int(input())
results = []

for _ in range(t):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))
    
    parent = list(range(n + 1))  # positions 1..n
    
    for i in range(1, n + 1):
        if i + x <= n:
            union(parent, i, i + x)
        if i + y <= n:
            union(parent, i, i + y)
    
    ok = True
    for i in range(1, n + 1):
        value = p[i - 1]
        if find(parent, i) != find(parent, value):
            ok = False
            break
    
    results.append("YES" if ok else "NO")

print("\n".join(results))