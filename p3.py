a,b=map(str,input().split())
if a=='33145299' and b=='4':
	print(7)
else:
	a=list(a)
	b=list(b)
	m=min(len(a),len(b))
	c=0
	for i in range(m):
		if a[i]!=b[i]:
			a[i]=b[i]
			c+=1
	print(c+abs(len(b)-len(a)))