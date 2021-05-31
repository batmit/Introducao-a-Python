n = int(input("Digite um número: "))
par = False
if n % 2 == 0:
    par = True
p = 1
quant = 0
while p <= n:
    div = n % p == 0 
    if div == True:
        quant += 1
    p += 1
if par == True and quant == 2:
    print("Esse é um número par e primo")