a=int(input())
s=1000
for i in range(0,20):
    if pow(2,i)<=a:
        x = abs(pow(2, i) - a)
        if x < s: s = x
print(s)