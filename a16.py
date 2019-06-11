s=input()

j=s[0]

for i in s:

    if s.count(j)>s.count(i):

        j=i

print(j)