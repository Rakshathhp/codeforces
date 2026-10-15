"""
n=str(input("enter n"))
n=list(n)
j=len(n)-1
i=0
while i<j:
    temp=n[i]
    n[i]=n[j]
    n[j]=temp
    i+=1
    j-=1
print("".join(n))

"""
a=str(input("enter a"))
original=a
a=a[::-1]
print(original)
print(a)

a=str(input("enter n"))
n=len(a)-1
res=""
for i in range(n,-1,-1):
    res+=a[i]
print(res)

