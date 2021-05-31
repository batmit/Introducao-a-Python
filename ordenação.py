# as listas vistas até agora não possuem uma lista organizada
# para fazer isso vamos usar o método Bubble Sort, que consiste em trocar de posição dois valores se 
# eles forem repetidos
l = [7, 4, 3, 12, 8] 
fim = len(l)
while fim > 1: # devemos repetir várias vezes, para que não tenha de fato nenhuma repetição 
    trocou = False
    x = 0
    while x < (fim - 1): # assim analisa 5 valores e não seis
        #vou analisar todos os valores da lista
        if l[x] > l[x+1]:
            trocou = True
            temp = l[x] # armaze-no o valor de l na posição 0 para o temp
            l[x] = l[x + 1] # e troco os valores
            l[x + 1] = temp
        x += 1
    if not trocou: # se depois de verificar toda a repetição não tiver trocado nada, saí da repetição
        break
    fim -= 1
for e in l:
    print(e)