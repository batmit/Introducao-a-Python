#podemos recuperar o valor de uma chave e, caso não exista, utilizar um calor padrão.
#utilizamos o método get
d = {}
for letra in 'abracadabra':
    #para cada letra na palavra,
    d[letra] = d.get(letra, 0) + 1
    #o método vai tentar obter a chave procurada, se não conseguir vai substituir por 0, o segundo valor. Se não colocar o segunda vira None
    #se achar a chave vai usar o valor já atribuído

print(d)

#d.get(letra, 0) => d pega a letra, se não achar coloca 0, depois acrescenta +1

# o método get pega o valor procurado, se não achar coloca ou None ou o que eu colocar em segundo, nesse caso o 0