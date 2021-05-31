# decimais

# quando formatamos números decimais usamos dois valores entre o símbolo % e a letra f
#o primeiro indica o tamanho total em caracteres a reservar, e o segundo mostra o número de casas decimais


a = 7

print("R$%4.2f" % a)

print("R$%10.2f" % a) #vai ter um baita espaço antes do número

print(f'R${a :4.2f}') # usando o format

print(f"{a:03}")# vai ficar 007
print(f"{a:<03}") # vai ficar 700

#interessante que o format é inteligênte e sabe diferenciar strings de int e flutuantes