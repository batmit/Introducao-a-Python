lugares_vagos = [10, 2, 1, 3, 0] # a posição desses números é as salas e o numero em sí é a quantidade de cadeiras livres
while True:
    sala = int(input("Qual sala você gostaria de reservar(0 sai): "))
    if sala == 0:
        print("fim")
        break
    if sala > len(lugares_vagos) or sala < 1: # vai ser inválido
        print("Quantidade de salas inválidas.")
    elif lugares_vagos[sala - 1] == 0:
        print("Lugares lotados")
    else:
        lugares = int(input(f"Quantos lugares você quer ({lugares_vagos[sala - 1]} vagos): "))
        if lugares > lugares_vagos[sala -1]:
            print("Esse número de lugares não está disponível")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos.")
print("Utilização de salas: ")
for x, l in enumerate(lugares_vagos):
    print(f"Sala{x + 1} - {l} lugares vagos")