r,s=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
for i in range(s):
	u,v=map(int,raw_input().split())
	c=l[u-1:v]
	print(sum(c))