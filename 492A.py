n=int(input())
cubes=n
b=1
rows=1
for i in range(2,n):
    cubes-=b
    b+=i
    if cubes<b:
        break
    else:
        rows+=1
print(rows)



