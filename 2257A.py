t=int(input())

for _ in range(t):
	n=[]
	m=[]
	
	a,b=map(int,input().split())
	for i in range(a):
		x=input()
		x=x.lower()
		n.append(x[0])
	for j in range(b):
		y=input()
		y=y.lower()
		m.append(y[0])
	c=0
	for ch in m:
		if ch in n:
			c+=1
			print("yes")
			break
	if c==0:
		print("no")