a=[
    #c1,c2,c3
    [1,2,3,5],     #r1 a[0]
    [4,5,6,8],     #r2  a[1]          0,0  0,1 0,2 0,3  1,0 1,3 2,0 2,1 2,2 2,3 
    [7,8,9,6]      #r3   a[2]
]
l=0
h=len(a)
out=[]
for i in range(h):
    for j in range(len(a[i])):
        if i==l or i==h-1:
            out=a[i][j]
            print(out)
    if i>0 and i<h-1:
        print(a[i][l],a[i][h])


