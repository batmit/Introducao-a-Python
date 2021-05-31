T = [-10, -8, 0, 1, 2, 5, -2, -4]
menor = T[0]
maior = T[0]
x = 0
for c in T:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
    x += c
print(f"O menor valor é: {menor}\nO maior valor é {maior}\nA média é: {x / len(T)}")