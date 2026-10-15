
a = list(map(int, input("Enter numbers separated by space: ").split()))
target=int(input("enter target"))
def sum2(n,target):
    for i in range(len(n)):
        result=target-n[i]
        for j in range(i+1,len(n)):
            if n[j]==result:
                return n[i]+n[j]     
           
    return None
a=sum2(a,target)
print(a)


a = list(map(int, input("Enter numbers separated by space: ").split()))
target=int(input("enter target"))
sums={}
for i in range(len(a)):
    x=target-a[i]
    if x in sums:
        print(sums[x], i)   # indices
        break
    sums[a[i]] = i
        
