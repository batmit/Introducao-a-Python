# o else também pode ser utilizado no bloco try, e else ocorre se não ouver execção no try e pode ser
# combinada com except e finally
while True:
    try:
        v = int(input("Digite um número inteiro(0 sai): "))
        #print("Parabéns, nenhuma exceção") # posso fazer assim, porque se alguém cometer um erro vai sair na hora
        if v == 0:
            break # o break já sai de tudo
    except Exception:
        print()
        print("Valor inválido! Tente novamente")
        print()
    else: # se refere ao except
        print("Parabéns, nenhuma exceção")
    finally:
        print("Executado sempre, mesmo com break")