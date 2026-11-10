n=int(input())
for _ in range(n):
    a=input().split()
    res=""
    for ch in a:
        res+=ch[0]
    print(res)