l = [-312, -543, -1321, -313, -1322, -1324, 2] # o 2 vai ser o maior :)
maior = l[0]
for c in l:
    if c > maior:
        maior = c # nesse caso fica salvo o c naquela posição na variável maior, então não tem problema
print(maior)