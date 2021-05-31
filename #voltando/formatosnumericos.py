# posso usar python e format para converter valores em vários tipos
# b = binário
# c = Caractere
# d = base 10
# n = base 10 local
# o = octal
# X ou x = hexadecimal om letras mmaiúsculas ou minúsculas, respectivamente
# e = notação científica com e minúsculo
# E = notação científica com e maiúsculo
# f = decimal
# g ou G = genérico
# n = local
# % percentual
print("{0:b}".format(60)) # vai mostrar o número em binário

#---------------- A diferença entre o de base 10 e o local é que o local pega configurações locais do dispositivo
# como estou no Brasil atualmente, vai usar , se eu mudar o local da máquina, vai usar . por exemplo ou whatever
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")
print("{:n}".format(5678)) # vai usar ponto ao invés da vírgula