# no python também podemos modificar posições das strings
# veja o modo center a seguir:
s = 'tigre'
print("X" + s.center(10) + "X") # coloco o s no centro a uma distância de 10, com X entre eles

print("X" + s.center(10, ".") + "X") # dou um espaço de 10 colocando ponto entre

#também podemos alinhar somente um dos espaços

print(s.ljust(10, ".")) # nesse caso uso um left just para colocar apenas um espaço para a esquerda preenchido
# com ponto

print(s.rjust(10, ".")) # mesma coisa só que ao contrário