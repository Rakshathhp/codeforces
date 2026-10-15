n = int(input())
a = list(map(int, input().split()))

police = 0
untreated = 0

for x in a:
    if x > 0:
        police += x
    else:
        if police > 0:
            police -= 1
        else:
            untreated += 1

print(untreated)