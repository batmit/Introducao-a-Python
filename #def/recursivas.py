# as funções recursivas são aquelas que chamas a elas mesmas.
# o problema do fatorial no #11.py nos resolvemos o fatorial chamando e executando
# o fatorial antecessor. Veja o exemplo da sequência fibonnaci:

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a = fibonacci(n - 1) + fibonacci(n - 2)
        return a
print(fibonacci(4))