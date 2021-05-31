#sempre que juntamos duas listas, quando modificamos uma, a outra automaticamente também muda
#se atentar a isso

papa = [0, 2, 4] #lembrando que isso cria uma lista

sd = papa[:]#a partir desse comando criamos uma variável diferente, uma cópia da antiga
# eu suponho que esse sinal de : pegue todo os números que estam dentro da variável

print(sd)

papa = [0,321,4 ]

print(sd)