l,r=map(int,input().split())

a=[]

for i in range(1,(l*r)+1):

	if (i%l==0 and i%r==0):

		a.append(i)

print(min(a))