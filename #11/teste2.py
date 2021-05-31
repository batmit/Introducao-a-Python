dic = {}
a = 'abc'
x = 0
for c in a:
    dic[c] = x # vou adicionar o c como chave e o x como value
    x += 1
print(dic)

# saco só como python é inteligente, quando você adiciona um valor a um dicionário só fazer dic[x] = 1 (ele já vai colocar em último)