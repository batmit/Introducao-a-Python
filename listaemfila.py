ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
while True:

    qual = input("Digite (primeira) para trabalhar com a primeira fila, e (segunda) para trabalhar com a segunda: ")

    if qual =="primeira":
        print(f"\nExistem {len(fila1)} clientes na fila1")
        print(f"Fila atual: {fila1}")
        print("Digite F para adicionar um cliente ao fim da fila1,")
        print("Ou A para realizar um atendimento. S para sair.")
        operação = input("Operação(F, A ou S):")
        if "A" in operação:
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido")
            else: 
                print("Fila vazia! Ninguém a atender")
        elif "F" in operação:
            ultimo1 += 1 # incrementa o ticket com mais uma pessoa 
            fila1.append(ultimo1)
        elif "S" in operação:
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!!!")


    elif qual == "segunda":
        print(f"\nExistem {len(fila2)} clientes na fila2")
        print(f"Fila atual: {fila2}")
        print("Digite F para adicionar um cliente ao fim da fila2,")
        print("Ou A para realizar um atendimento. S para sair.")
        operação = input("Operação(F, A ou S):")
        if "A" in operação:
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido")
            else: 
                print("Fila vazia! Ninguém a atender")
        elif "F" in operação:
            ultimo2 += 1 # incrementa o ticket com mais uma pessoa 
            fila2.append(ultimo2)
        elif "S" in operação:
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!!!")


    else:
        print("Operação inválida! Digite apenas (primeira) ou (segunda)!!!!")