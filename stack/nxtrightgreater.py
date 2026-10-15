n=list(map(int,input("enter: ").split()))
st=[]
for i in range(len(n)):
    f=0
    for j in range(i+1,len(n)):
        if n[i]<n[j]:
            st.append(n[j])
            f=1
            break
    if not f:
        st.append(-1)

print(st)