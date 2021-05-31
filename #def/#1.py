# def, finalmenteeeee
def soma(a, b):
    print(a + b) # a função vai fazer nada mais nada menos que devolver na tela a + b, sendo que os valores de
    # a e b seram adicionados depois.
soma(2, 9)
soma(7, 8)
soma(10, 15)

# só será retornada o valor assim que chamarmos a função e definirmos um valor para a e outro para b, mas também podemos:
def soma(a, b):
    return a + b
print(soma(2, 9)) # nesse caso eu tenho que imprimir na tela pois o return não propriamente imprime,na função de
# cima eu tinha de fato colocado um print, mas aqui não
a = soma(10, 15) # adiciona a uma variável
print(a)

def épar(x):
    return x % 2 == 0 # vai retornar uma condição, isso é incrívellllllllllllllllll
print(épar(2))
print(épar(11))

def par_ou_impar(x):
    if épar(x): # o x vai ser o valor enviado depois, vamos usar o x para realizar a função acima
        return "par" # tudo depois do return é imediatamente desconsiderado, como se fosse um continue
    else:
        return "impar"
print(par_ou_impar(11))