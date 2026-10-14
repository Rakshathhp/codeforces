a=list(map(int,input().split()))
b=set(a)
print(len(a)-len(b))


"""
or
a = list(map(int, input().split()))
print(4 - len(set(a)))
"""