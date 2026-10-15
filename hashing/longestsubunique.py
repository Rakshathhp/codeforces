a = input("enter: ")

seen = {}
start = 0
maxi = 0

for i in range(len(a)):
    if a[i] in seen and seen[a[i]] >= start:
        start = seen[a[i]] + 1

    seen[a[i]] = i
    maxi = max(maxi, i - start + 1)

print(maxi)
