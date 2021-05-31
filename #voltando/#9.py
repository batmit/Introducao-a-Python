a = input("Digite a primeira  string: ")
b = input("Digite a segunda string: ")
c = b in a
if c == True:
    print(a.find(b)) # vou buscar a posição de b
else:
    print("Desculpe, o b não está dentro do a")