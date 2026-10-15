a=str(input("enter a"))
b="aeiou"

put=""
without=""
for i in range(len(a)):
    if a[i] not in b:
        put+=a[i]
    else:
        without+=a[i]
print("without vowels",put)
print("vowels are",without)

final=""
for i in range(len(without)):
    f=0
    c=1
    for j in range(i+1,len(without)):    
        if without[i]==without[j]:
            f+=1
            c+=1
    if f>0 and c>1 and without[i] not in final:
        final+=without[i]
        print(c,without[i])
print("repeted vowels",final)
print(len(final))


def unique(a):
    res=""
    count=1
    for i in range(len(a)):
        if a[i] not in res:
            res+=a[i]
    return res
result=unique(a)
print("unique ele in string=",result)

repeted=unique(without)
print("vowels are=",repeted)