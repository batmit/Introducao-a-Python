# podemos também desenpacotar parâametros usando python

def soma(a, b):
    print(a + b)
L = [2, 3]
soma(*L) # esse * vai desempacotar os parâmetros apresentados, como tem dois vai enviar os dois, subsistue o for
