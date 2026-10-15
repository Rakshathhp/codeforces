a=[
    #c1,c2,c3
    [1,2,3,5],     #r1 a[0]
    [4,5,6,8],     #r2  a[1]    
    [7,8,9,6]      #r3   a[2]
]
r=len(a)
c=len(a[0])
for i in range(c):
    c=[]
    for j in range(r):
       c.append(a[j][i])
    c.reverse()
    print(c)

