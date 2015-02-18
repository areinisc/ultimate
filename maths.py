outer = [1,2,3,4,5,6]
inner = [1,2,3,4,5,6]
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for roll in outer:
    for rol in inner:
        if abs( roll - rol) == 0:
            a = a + 1
        elif abs( roll - rol) == 1:
            b = b + 1
        elif abs( roll - rol) == 2:
            c = c + 1
        elif abs( roll - rol) == 3:
            d = d + 1
        elif abs( roll - rol) == 4:
            e = e + 1
        elif abs( roll - rol) == 5:
            f = f + 1
print a
print b
print c
print d
print e
print f
