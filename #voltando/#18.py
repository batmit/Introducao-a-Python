#Formatação de strings com format
a = "{}, {}".format("batata", "arroz") # esse é o método tradicional
print(a)
# também tem o método de separar por números os valores:
b = "{1}, {0} and {1}".format("to", "lele")
print(b)
# nesse caso o 1 dentro das {} representa o variável dentro do format que vai pegar, nesse caso o "lele"
# posso inclusive inverter a ordem das palavras
c = "{1}, {0}".format("primeiro", "segundo")
print(c)
print("{0:10}, {1}".format("123", "456")) # vai usar 10 de espaço, vai enfiando até achar lugar
print("X {0:>10} X".format("123")) # vai jogar para a direita
print("X {0:^10} X".format("123")) # vai colocar entre
print("X {0:.^10} X".format("123")) # vai colocar os pontos entre
print("X {0[0]:.^10} {0[1]:.^10} X".format(["123", "456"])) #como é uma lista devemos especificar os valores
print(f"X {123:.^10} X")