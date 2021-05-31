frase = input("Digite uma frase para contar as letras:")
d = {}
for letra in frase:
    if letra in d:
        d[letra] = d[letra] + 1 # acesso a chave, que já existe e substituo tudo
    else:
        d[letra] = 1
print(d)