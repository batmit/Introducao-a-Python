def verificação(string, lista):
    if string in lista:
        return True, "Está certo"
    else:
        return False, "Infelizmente a string não está na lista"

print(verificação("batata", ["batata", "maça", "banana", "limão"]))