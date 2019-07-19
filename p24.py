ll = int(input())
rest = []
for i in range(pow(2, ll)):
    rest.append(bin(i)[2:].zfill(ll))
rest.sort(key=(lambda x: x.count('1')))
for i in rest:
    print(i) 