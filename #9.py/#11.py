# for é uma estrutura de repetição usada essencialmente para listas, a cada repetição um novo termo da lista é utilizado
l = [1, 5, 6, 3]
x = 0
for c in l:
    print(c) # o c representa cada valor dentro do l, a cada repetição esse valor fica maior
    x += 1
print("-" * 20, x)

# o for é mais utilizado quando trabalhamos com listas, mexemos em elementos sequenciais e sabemos quantas vezes vamos repetir um número
