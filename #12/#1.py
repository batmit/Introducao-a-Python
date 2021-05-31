#tuplas
#tuplas são parecidas com listas mas são imutáveis

tupla = ("a", "b", "c", "a") # eu também posso usar sem parênteses
print(tupla)

#também podemos usar aqueles artifícios de visualização de listas:
print("_+_" * 100)
print(tupla[0:])

#mas não podemos mudar os valores
print("_+_" * 100)
#usando for: 

for c in tupla:
    print(c)