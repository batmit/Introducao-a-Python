#podemos recuperar o valor de uma chave e, caso não exista, utilizar um calor padrão.
#utilizamos o método get
d = {}
for letra in 'abracadabra':
    #para cada letra na palavra,
    print(letra)
    d[letra] = d.get(letra, 0) + 1
    #o método vai tentar obter a chave procurada, se não conseguir vai substituir por 0, o segundo valor. Se não colocar o segunda vira None
    #se achar a chave vai usar o valor já atribuído

print(d)
# a partir do momento que não tem nada fica 1, quando já tem o letra recebe o valor dentro da chave

#d.get(letra, 0) => d pega a letra, se não achar coloca 0, depois acrescenta +1