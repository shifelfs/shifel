def findstem(arr): 
	n = len(arr) 
	s = arr[0] 
	l = len(s) 
	res = "" 
	for i in range( l) : 
		for j in range( i + 1, l + 1) : 
			stem = s[i:j] 
			k = 1
			for k in range(1, n): 
				if stem not in arr[k]: 
					break
			if (k + 1 == n and len(res) < len(stem)): 
				res = stem 

	return res 
if __name__ == "__main__": 
	
	arr = []
	num=int(input())
	for i in range(num):
	    string=input()
	    arr.append(string)
	stems = findstem(arr) 
	print(stems) 
