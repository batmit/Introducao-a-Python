while True:
    palavra = input("Digite uma palavra para ser lida(0 sai): ")
    if palavra == '0':
        break
    baralho = {}
    x = 0
    for c in palavra: #mandei bem, vou pegar cada letra
        if c in baralho: # se a letra já está no baralho
            baralho[c] = baralho[c] + 1 # eu vou mudar, acesso a chave e substituo tudo
        else:
            baralho[c] = 1 # aqui eu defino c como a chave e 1 como o  value
        x += 1
    print(baralho)