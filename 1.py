//print the max occurence of number and the number by concatenating the list
l=list(input().split())
a=""
b=[]
for i in l:
  a=a+i
for i in range(0,10):
  i=str(i)
  c=a.count(i)
  b.append(c)
m=max(b)
print(m)
for i in range(0,10):
  if b[i]==m:
    print(i,end=" ")
  