a,n,d=input().split()
a=int(a)
n=int(n)
d=int(d)
sum=0
ap=a
for i in range(n):
    ap=a+d
    sum=sum+ap
print(sum)
