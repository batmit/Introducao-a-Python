# para verificação de valores podemos usar starstwith e endswith
# ends e starts
nome = "João da Silva Larangeiro"
print(nome.startswith("João")) #verifica se o nome começa com o João ou não, retornando um True ou False
print(nome.endswith("Larangeiro"))# verificar se o nome ends with a palavra

#importante destacar que existe uma diferença entre letras maiúsculas e minúsculas. Para resolver essa diferença convertemos a variável

print(nome.lower().startswith("joão")) #vou pegar o nome usando a função lower verificando se começa com joão,
# a função lower converte para minúsculo, tudo para minpusculo
print(nome) # veremos que continua maiúsculo
nome = nome.lower() # a função nome vai passar a receber a função nome minpuscula
print(nome)

nome = nome.upper()
print(nome) # nome recebe a função nome com tudo maiusculo

print(nome.startswith("JOÃO")) # vai retornar True