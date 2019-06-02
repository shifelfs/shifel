import math
a,b=map(int,input().split())
c=a*b
root = math.sqrt(c)
if int(root + 0.5) ** 2 == c:
    print("yes")
else:
    print("no")
