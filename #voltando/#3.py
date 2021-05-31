#para comparar as strings devemos usar os comandos aprendidos anteriormente

a = "João da Silva Figueiredo"
print("João" in a) # vai retornar verdadeiro
print("joão" in a) # vai retornar False
print("J" or "j" in a) # vai retornar J. estou perguntando se tem J ou j, aí ele responde J
print("Silva" or "silva" in a) # estou perguntando qual tem a
print("João".upper() in a) # vai retornar False
print("JOÃO" in a.upper())

#além do in dá para usar not in

print("João" not in a) # vai retornar false, obviamente
print("João" not in a.upper())# vai retornar True, porque não está
print("joão" not in a.lower()) # vai retornar False