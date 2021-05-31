#quando adicionamos um terceiro valor ao range, queremos dizer a quantidade de casas que vai pular, no caso abaixo vai de três em três
for t in range(3, 33, 3): #mostra os múltiplos de 3, os dez primeiros múltiplos de 3
    print(t, end=" ")
print()# nesse caso pula uma linha
# sempre importante entender que o range não é uma lista, para fazer com que ele repita os valores é preciso usar uma repetição, ou transforma-lo em lista