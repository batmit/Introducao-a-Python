n1 = 0
a = 247
b = 576
c = 0
while c < 100:
    e = 0
    while e < 1000:
                
        a = a + (a ** b)
        n1 += a
        e += 1
        print(n1)
    c += 1

print(n1)