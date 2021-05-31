a = input("Digite algo: ")
b = input("Digite algo: ")
c = input("Digite algo: ") #sem o int é considerado uma string

Z = [a, b, c, 20, 30, 'batata'] #isso mostra que é uma lista

r = len(Z) #lembrar que uma lista começa do 0, logo tem que diminuir 1 

print(Z)

print(Z[r - 1])