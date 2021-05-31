#lista como pilhas, as pilhas são retiradas o último primeiro
pratos = 5
pilha = list(range(1, pratos + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("Ou D para desempilhar. S para sair.")
    operação = input("Operação(E, D ou S): ")
    if operação == 'E':
        prato += 1 #novo prato
        pilha.append(prato) #adiciona o número final de pratos
    elif operação == 'D':
        if len(pilha) > 0:
            lavado = pilha.pop(-1) # vai tirar o último
            print(f"Prato {lavado} lavado!")
        else:
            print("Operação inválida! A pilha está vazia meu consagrado!")
    elif operação == 'S':
        break
    else:
        print("Operação inválida! Digite apenas D, S ou E!!!")