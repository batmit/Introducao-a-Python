a = input("Digite a primeira string: ")
b = input("Digite a segunda string: ")
c = set(a)
d = set(b)
if d > c:
    e = d - c
else:
    e = c - d
print("Diferentes: ", e)