a=[
    #c1,c2,c3
    [1,2,3],     #r1 a[0]
    [4,5,6],     #r2  a[1]          0,0  1,2 2,2
    [7,8,9]      #r3   a[2]
]
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==j:
            print(a[i][j])