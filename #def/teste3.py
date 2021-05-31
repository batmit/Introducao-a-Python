a = 5
def muda_e_imprime():
    #print(a) não funciona, para fazer a variável a vim para cá preciso passar como parâmetro
    a = 7 # o a que criamos aqui é apenas a variável local, não é global
    print(a)
print(a)
muda_e_imprime()