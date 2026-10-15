s=str(input("enetr s"))
space=0
digit=0
r=""
for ch in s:
    if ch==" ":
        space+=1
    elif ch.isdigit():
        digit+=1
    else:
        r+=ch
print(space)
print(digit)
print(r)