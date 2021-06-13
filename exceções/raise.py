# o raise é outro tipo de exceção
nomes = ["Ana", 'Carlos', 'Maria']
try:
    i = int(input('Digite o índicie que quer imprimir: '))
    print(nomes[i - 1])
except ValueError as e:
    print('Digite um número!')
    raise # o raise mostra o código de erro depois do print acima e depois do finally
finally:# o finally é executado sempre, e é executado antes do raise
    print("O finally é sempre executado")
# explicação: primeiramente se executa o try, depois que tem o erro se mostra o print dentro do erro, então mostra
# o finally e depois mostra o código do erro, que é executado pelo raise

# veja o exemplo a seguir em que usamos o bloco try dentro de uma função
def épar(x):
    try:
        return x % 2
    except Exception:
        raise ValueError("Valor inválido")# nesse caso "criamos" nosso código de erro, ele vai mostrar a mensagem
        # de erro depois de mostrar o erro que aconteceu
    # se eu quiser não mostrar o erro original deve usar:
    #    raise ValueError("Valor inválido") from None # esse from None vai eliminar o código de erro original
    finally:
        print("Executado antes do return") # como o return dá um break esse print é executado antes
        # quando acontece o return ele verifica
try:
    print(2, épar(2)) # vai dar certo
    print("A", épar("A"))# vai dar errado
except Exception:
    print("Algo de errado não está certo! ")
