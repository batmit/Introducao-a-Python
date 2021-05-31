l = [0] * 10
print(l) # essa é a lista

# a função hash no python é uma forma de espalhamento que gera um número aleatório, pelo que entendi

print(hash("A")) # gera um valor na string "A", um hash

# esse 10 representa o número de índicies que quero colocar, ele é o número de l, o len(l)
print(hash("A") % len(l)) # temos um índicie, gera um índicie aleatório. de 0 a 9(isso porque o número de índicies escolhido é o 10)

l[hash("A") % 10] = 'A' # pega o l na posição do índicie gerado e coloca o "A" la
print(l)