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
terceira = primeira[:] #quando ele copia os números, ele não repete
terceira.extend(segunda)#eu não posso usar o append nem o +=, porque eles somente adicionam valores que não existem
x = 0
while x < len(terceira):
    print(f"{terceira[x]}")
    x += 1
print(terceira)