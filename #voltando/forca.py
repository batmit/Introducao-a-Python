from time import sleep
# intro
print("-"*10 + "Forcaaaaaaaaaa" + "-"*10)
palavras = [["batata", "vegetal amarelo"], ["bicicleta", "andamos nela"], ["maça", "a eva comeu"], ["brasil", "país sem liberdade econômica"], ["irineu", "você não sabe nem eu"]]
numero = int(input("Digite um número inteiro que será utilizado para sortear a palavra a ser descoberta: "))
indicie = (numero * 776) % len(palavras)
palavra = palavras[indicie][0]
dica = palavras[indicie][1]
print("\n" * 20)
acertos = []
tentativas = [] # as palavras tentadas até então
erros = 0
chances = ["|", "|", "|", "|", "|", "|"]
letras = []
forca = []
for c in palavra: # para saber quantas letras compoem a palavra, para poder contar o número de acertos
    if c not in letras:
        letras.append(c)
while True:
    print("\n" + "-"*100 + "\n")
    # imprimir letras descobertas até então
    for c in palavra:
        if c in acertos:
            print(c, end="")
        else:
            print(".", end="")
    print()
    # qual operação vai fazer
    jogada = int(input("""Digite a operação: 
        [0] Ver Dica
        [1] Tentar uma letra
        : """))
    # se jogou errado
    if jogada != 0 and jogada != 1:
        print("Jogada inválida, tente novamente")
        continue
    # se quer ver a dica
    elif jogada == 0:
        sleep(1)
        print("Dica: ", dica)
        sleep(2)
        continue # vai voltar para o começo
    # se quer jogar
    elif jogada == 1:
        print("Boneco: " ,"".join(forca))  # boneco da forca
        print("\n" + "Chances: ", chances, "\n")
        print("Tentadas até então: ", tentativas)
        chute = input("Digite a letra: ").lower().strip() # vou tirar os espaços vazios
        # se já tentou antes
        if chute in tentativas:
            sleep(1)
            print("\n" + "Você já tentou essa! Tente novamente")
            continue
        tentativas.append(chute)
        # se acertou
        if chute in palavra:
            sleep(1)
            print("Você acertou. " + "\n")
            sleep(1.4)
            acertos.append(chute)
            if len(acertos) == len(letras):
                # se a quantidade de letras acertadas for igual a quantidade de letras na palavra
                print("Parabéns, você ganhou!")
                break
        # se errou
        else:
            sleep(1)
            print("Você errou!" + "\n")
            sleep(1.4)
            erros += 1
            leno = len(chances)
            if erros == 1:
                forca.append("X")
            elif erros > 1 and erros <= 5:
                forca.append("-")
            elif erros == 6:
                forca.append("|")
            del chances[leno - 1]
            if erros == 6:
                print("".join(forca))  # boneco da forca
                for c in palavra:
                    if c in acertos:
                        print(c, end="")
                    else:
                        print(".", end="")
                print("\n" + "Chances: ", chances, "\n")
                print("Acabou o jogo, você perdeu!")
                print("A palavra era: ", palavra)
                break