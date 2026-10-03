n=int(input())
a=str(input())
b=str(input())
c=[]
d=[]
for i,digit in enumerate(a):
    c.append(digit)
print(c)
for i,digit in enumerate(b):
    d.append(digit)
print(d)
test=[]
for i in range(0,9):
    test.append(i)
for i in range(9,0-1,-1):
    test.append(i)
print(test)
