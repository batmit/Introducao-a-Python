# as funções em python não aceitam o uso de variáveis locais a não ser que seja como parâmetro, para mudar
# isso devemos usar local antes da variável
# É sempre bom evitar usar variáveis globais e deixar elas mais com um valor fixo ou constante
a = 10
def change():
    # se eu colocar um print(a) aqui não vai funcionar, pois o a é uma variável global que está fora da função
    global a # a partir de agora na função vou sempre usar a variável global e não a local
    # importante destacar que para o computador variáveis locais e globais são totalmente diferentes, totalmente
    a = 11
    print(f"A durante a mudança: {a}")

print(f"A antes da mudança: {a}")
change() # então eu chamo a função
print(f"A depois da mudança: {a}")

# def lele():
#     print("Sou lele")
# lele()