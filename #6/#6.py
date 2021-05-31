while True:
    valor = float(input("Digite o valor a pagar: "))
    if valor == 0:
        break
    cédulas = 0
    atual = 100 #vamos considerar a maior a atual
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
        else:
            print(f"{cédulas} cédulas de R${atual:.2f}")
            if apagar == 0:
                break
            elif atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.1
            elif atual == 0.1:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            elif atual == 0.01:
                atual = 0.001
            cédulas = 0 #sempre zero no final
print("Bye bye :)")