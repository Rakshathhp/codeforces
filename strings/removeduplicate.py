n=10
for i in range(n):  
    a=str(input("enter a"))
    b=""
    res=""
    max_count=0
    max_char=""
    for i in range(len(a)):
        count=1
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                count+=1
                if a[i] not in b:
                    b+=a[i]
        if count>max_count:
            max_count=count
            max_char=a[i]
        elif count==max_count and a[i] not in max_char:
            max_char+=a[i]
    if len(b)==0:
        print("no duplicate values")
    else:
        print("duplicates values are",b)
    for i in range(len(a)):
        case=0
        for j in range(len(b)):
            if a[i]==b[j]:
                case+=1
        if case==0:
            res+=a[i]
    if len(res.strip())==0:
        print("no unique numberes")
    else:        
        print("unique values are",res)
    print(max_char,max_count)


