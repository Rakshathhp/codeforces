n=int(input())
for _ in range(n):
    m=int(input())
    s=list(map(int,input().split()))
max_c=0
ans=None
for i in range(len(s)):
    count=1
    for j in range(len(s)):
        if s[i]==s[j]:
            count+=1
    if max_c<count:
        max_c=count
        ans=s[i]
print(ans)

    