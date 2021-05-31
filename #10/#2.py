l = [34, 54, 77]
for z in enumerate(l): # nesse caso o z recebe os dois valores, o índice e o número dentro do l
    x, c = z
    print(f"Número: {c} na posição: {x}")
    print(z)