n=int(input())
if(n<60):
	print("0",n)
else:
	hr=n//60
	min=n%60
	print(hr,min)