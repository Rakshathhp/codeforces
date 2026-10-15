a=input("enter: ")
b=[]
for i in a:
    b.append(i)

while b:
    """or while len(b)>0 both same"""
    print(b.pop(),end="")

"""or"""
for j in range(len(b)):
    x=b.pop()
    print(x)