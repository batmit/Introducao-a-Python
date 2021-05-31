# podemos também validar strings, apenas strings
s = '125'
p = 'AlÔ Mundo'
print(s.isalnum()) # vai verificar se o s tem todos os caracteres preenchidos, sem espaços vazios
print(p.isalpha()) # vai verificar se são todos letras, sem caracteres especiais e sem espaços
print("641".isdigit()) # verificar se contem
# apenas números, sem caracteres especiais e espaços vazios
print("10.45".isdigit())
# o isdigit não inclui frações e tal, já o isnumeric inclui
print("10.45".isnumeric()) # ainda não aceitou o ponto

# também podemos ver se é tudo maiúsculo ou tudo minúsculo
print("BATATA".isupper(), "maça".islower()) # vai retornar true true


# também tem como verificar se tem espaço
print("Olá\nlele".isspace()) # nesse caso se verificou uma quebra de linha
print("\tLele".isprintable()) # nesse se verificou se pode se priintar o conteúdo
# como \t é uma função não pode