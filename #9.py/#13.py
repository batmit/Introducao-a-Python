# a função range é usada para gerar listas simples e práticas
# a função range não gera uma lista propriamente dita, mas um generator

for c in range(10): # lembre-se que printa só até o penúltimo
    print(c)

lele = list(range(10))
print(lele)
print(range(10)) # não gera uma lista, apenas um generator, ele precisa ser atribuída a uma lista para conseguir mostrar todos os valores

