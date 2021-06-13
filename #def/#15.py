def verificação(string):
    string.lower()
    while True:
        lele = input("Digite uma opção: ").lower()
        for c in lele:
            if c in string:
                return True
            else:
                print("Tente novamente")
                break
print(verificação("abcsdfagtewtasfasr"))