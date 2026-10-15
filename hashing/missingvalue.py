r = list(map(int, input("enter: ").split()))
s=set(r)
for i in range(1,len(r)+2):
    if i not in s:
        print(i)
        break


"""
a=list(input("enter").split())
suma=0
for i in range(len(a)):
    suma+=int(a[i])
n=len(a)+1
exceptsum=n*(n+1)//2
miss=exceptsum-suma
print(miss)

"""