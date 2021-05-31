while True:
    numeros = int(input("Quantos números primos ver: "))
    if numeros == 0:
        break
    varios = 0
    n = 0
    while varios < numeros: 
        p = 1
        quant = 0
        while p <= n:
            div = n % p == 0 
            if div == True:
                quant += 1
            p += 1
        if quant == 2:
            print(n)
            varios += 1
        n += 1