a,b=map(int,input().split())
score=list(map(int,input().split()))
c=[]
for i in score:
    if i>=score[b-1]:
        if i !=0:
            c.append(i)
print(len(c))