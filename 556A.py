n=int(input())
a=input()
one=0
zero=0
for i in a:
    if i=='1':
        one+=1
    else:
        zero+=1
print(abs(one-zero))