# a função range gera uma sequência de elementos, mais um a cada chamado, ele é um generator
l = list(range(101)) # essa função transforma em uma lista a repetição de 0 até 100, geradas pelo range
# a função list tranforma os elementos apresentados em uma lista

print(l)

print("_" * 100)

del l[1:99]

print(l)

# list transforma em uma lista e range gera uma repetição de números, que pode ser melhor configurada


print("_" * 100)

print(range(101)) # isso não iria funcionar, devemos, eu e você, passas esses valores para uma lista, para que eles fiquem salvos