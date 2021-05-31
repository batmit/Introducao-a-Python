while True:    
    l = [1, 2, 3, 4, 5, 7, 9, 10, 12]
    p = int(input("Digite um número para pesquisar: "))
    for c in l: #lembrar que o c representa o l em uma determinada posição
        print(c)
        if c == p:
            print("Elemento encontrado!!!")
            break
    else: # é interessante notar que esse else é um else do for, se analisar tudo e nada acontercer, da o else
        print("Elemento não encontrado")