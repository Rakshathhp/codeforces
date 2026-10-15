"""
r = int(input("enter r"))
c = int(input("enter c"))

mat = []

for i in range(r):
    row = list(map(int, input().split()))
    mat.append(row[:c])

# Print matrix
for row in mat:
    print(*row)
    print("row sum",sum(row))
    """
a=[
    #c1,c2,c3
    [1,2,3],     #r1 a[0]
    [4,5,6],     #r2  a[1]
    [7,8,9]      #r3   a[2]
]
print("rows=",len(a))
print("columns=",len(a[0]))
r=0
c=0

for i in range(len(a)):
    r=0
    for j in range(len(a[i])):
        r+=a[i][j]
    print(f"row {i+1} count is",r)
for i in range(len(a)):
    c=0
    for j in range(len(a[i])):
        c+=a[j][i]
    print(f"column {i+1} count is",c)


