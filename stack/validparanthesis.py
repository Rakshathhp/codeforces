a=input(("enetr brackets: "))
s=[]
pairs={')':'(',']':'[','}':'{'}
valid=True
for ch in a:
    if ch in"({[":
        s.append(ch)
    else:
        if not s or s.pop()!=pairs[ch]:
            valid=False
            break
if valid and not s:
    print(True)
else:
    print(False)