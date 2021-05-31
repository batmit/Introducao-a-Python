primeira = input("Digite a primeira string: ") # aattcgaa
segunda = input("Digite a segunda string: ") #  tg
terceira = input("Digite a terceira string: ") # ac
quarta = []
if len(segunda) == len(terceira): # os valores tem que ser iguais
    for letra in primeira: # vou verificar todos os valores da primeira
        if letra not in segunda: # se não tiver na segunda prossiga
            quarta.append(letra)
        else: # se tiver na segunda...
            lele = segunda.find(letra) # verifique a posição da letra na segunda
            quarta.append(terceira[lele]) # coloque a terceira na posição da letra que é comum
    print("".join(quarta))
else:
    print("O valor da segunda e da terceira devem conter o mesmo número de caracteres")