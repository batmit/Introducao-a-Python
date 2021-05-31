primeira = []
segunda = []
while True:
    list1 = input("Digite algo para a primeira lista: ")
    if list1 == '0':
        break
    primeira.append(list1)
while True:
    list2 = input("Digite algo para a segunda lista: ")
    if list2 == '0':
        break
    segunda.append(list2)
x = 0
z = 0
print(primeira)
print(segunda)
terceira = primeira[:]
while x < len(segunda):
    y = 0
    z = 0
    while y < len(primeira):
        if segunda[x] == primeira[y]:
            z += 1
        y += 1
    if z == 0:
        terceira.append(segunda[x])
    x += 1
x = 0
while x < len(terceira):
    print(f"{terceira[x]}")
    x += 1
print(terceira)