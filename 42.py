s1,s2=map(str,input().split())
c1=0
c2=0
for i in s1:
      c1=c1+1
for j in s2:
      c2=c2+1
if(c1<c2):
      print(s2)
elif(c1==c2):
      print(s2)
else:
      print(s1)
