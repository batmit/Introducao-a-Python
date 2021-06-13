def soma(a, b):
    print(a + b)
L = [2, 3]
soma(*L) # 0 * manda todos os valores dentro do L

def imprime_maior(mesangem, *números): # o * desempacota os valores dentro de números
    maior = None
    for e in números:
        if maior is None or maior < e: # para usaro None como parâmetros devemos usar
            # o is None. is None
            maior = e
    return print(mesangem, maior)
imprime_maior("maior: ", 5, 4, 3, 1) # aqui eu não tenho que usar o * porque já mando separado
imprime_maior("max: ", *[2, 7, 9]) # aqui eu tenho que usar * porque enviei em formato de lista
imprime_maior("max: ") # vai enviar None, isso porque não passou números como parâmetro, o mensagem é
# obrigatório por ser requisitado para o print()