n=int(input())
l=list(map(int,input().split()))[:n]
p=len(l)//2
g=0
x=l[p:]
y=l[:p]
if (sum(x)//len(x))==(sum(y)//len(y)):
    g=1
if(g==1):
    print("yes")
else:
    print("no")