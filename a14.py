n=int(input())

l1=list(input())

l2=set(['a','e','i','o','u','A','E','I','O','U'])

b=list(filter(lambda x: x not in l2, l1))

print("".join(b[::-1]))
