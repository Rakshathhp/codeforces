s=input("input")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)
for i in freq:
    f=False
    if freq[i]==1:
        f=True
        break
print(i)
def dup(freq):
    for j in freq:
        c=0
        if freq[j]>1:
            c=1
        if c==1:
            return True
        else:
            return False
a=dup(freq)
print(a)
