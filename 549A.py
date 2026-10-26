n,m=map(int,input().split())
grid=[]
for _ in range(n):
    grid.append(input())
res=0
for i in range(n-1):
    for j in range(m-1):
        ch=[grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1]]
        if sorted(ch)==['a','c','e','f']:
            res+=1
print(res)