a = input().lower()

for ch in reversed(a):
    if ch.isalpha():
        if ch in "aeiouy":
            print("YES")
        else:
            print("NO")
        break
