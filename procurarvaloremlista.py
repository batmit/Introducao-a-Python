lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#==============================================================
while True:
    entrada = input("Digite um valor para acrescentar na lista.(0 sai do programa): ")
    if entrada == '0':
        break
    else:
        lista.append(entrada)
#---------------------------------------------------------------- 
    n1 = input("Digite o valor para procurar: ")
    n2 = input("Digite o valor para procurar: ")
    x = 0
    y = 0
#--------------------------------------------------------------
    while x < len(lista):
        if lista[x] == n1:
            break
        x += 1
#-----------------------------------------------------------------
    while y < len(lista):
        if lista[y] == n2:
            break
        y += 1
#----------------------------------------------------------------
    if x < len(lista): #se ele for verdadeiro
        print(f"O valor {n1} foi achado na posição {x + 1}")
    else:
        print(f"O valor {n1} não está em nossa lista, lamento")
#------------------------------------------------------------------
    if y < len(lista): #se ele for verdadeiro
        print(f"O valor {n2} foi achado na posição {y + 1}")
    else:
        print(f"O valor {n2} não está em nossa lista, lamento")