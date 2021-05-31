while True:
    def fatorial(n):
        fat = 1
        x = 1
        while n > x:
            fat *= n
            n -= 1
        return fat
    a = int(input("Digite um número para ser calculado o fatorial(0 dá o break): "))
    if a == 0:
        break
    print(f"Fatorial: {fatorial(a)}")