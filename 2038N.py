t=int(input())
for _ in range(t):
    n=input()
    a=int(n[0])
    b=n[1]
    c=int(n[2])
    if a<c and b=="<":
        print(n)
    elif a>c and b==">":
        print(n)
    elif a>c and b=="=":
        print(f"{a}>{c}")
    elif a<c and b=="=":
            print(f"{a}<{c}")
    elif a==c and b=="=":
        print(n)
    elif a<c and b==">" or b=="=":
        print(f"{a}<{c}")
    elif a>c and b=="<" or b=="=":
            print(f"{a}>{c}")
    else:
         print(a,"=",b)
    
