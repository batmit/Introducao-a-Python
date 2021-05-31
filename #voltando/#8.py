a = input("Digite a primeira string: ")
pasta = []
for letra in a:
    if letra not in pasta: # para não repetir
        print(letra, ": ", a.count(letra))
    pasta.append(letra) # tem que colocar depois, senão não vai fazer o if em nenhuma