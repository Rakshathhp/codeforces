a=input("enter a")
b=input("enter a")
a=list(a)
b=list(b)
def sor(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
a=sor(a)
a="".join(a)
print(a)
b=sor(b)
b="".join(b)
print(b)
if a==b:
    print("anagram")
else:
    print("not an anagram")