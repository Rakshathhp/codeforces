a=[
    #c1,c2,c3
    [1,2,3,5],     #r1 a[0]
    [4,5,6,8],     #r2  a[1]    0,0 0,1 0,2 0,3 1,3  2,3 2,2 2,1 2,0 1,0 1,1 1,2
    [7,8,9,6]      #r3   a[2]
]
r=len(a)+1
c=len(a[0])
for i in range(c):
    for j in range(r):
        if j<=i:
            print(a[i][j])
