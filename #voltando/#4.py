#para contar quanntas vezes algo repete usamos o método count

t = "um tigre, dois tigres, três tigres"
print(t.count("tigre")) # vai responder 3
print(t.count("t"))

#para proocurar usamos o find
print()
s = "Alô mundo" # lembrar que espaço vazio ocupa sim posição em uma string
print(s.lower().find('mun')) # vai retornar 4, que é a posição da string
print(s[3]) # vai retorar um valor vazio
print(s.find("ok"))
print(s.find("lele"))# como esse valor não exsite vai retornar -1, um valor negativo e não False
print(s.find("o")) # se tivesse dois o iguais pegaria somente o primeiro

#para achar a posição da direita para a esquerda se usa rfind

print()
t = "Um dia de sol"
print(t.rfind("d")) # vai pegar o primeiro d da direita para a esquerda
print(t.find("d")) # vai pegar o primeiro d da direita para a esquerda

#o rfind (right find) pega o primeiro valor da direita para a esquerda e apresenta a posição dele