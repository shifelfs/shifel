from itertools import combinations
a,b=map(int,input().split())
x=len(str(a))
l=list(combinations(str(a),x-b))
l=(sorted(l))
y="".join(l[0])
print(y)