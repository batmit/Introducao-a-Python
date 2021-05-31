s = [ "maças", "peras", "bananas", "paralelepípedo", "feijão com macarrão"]
#print(s[0]) # vai mostrar o elemento na posição 0 do s
#print(s[0][0]) # vai mostrar o elemento que está na posição 0 da posição 0 do s
#print(s[0][1]) # vai mostrar o elemento que está na posição 1 do elemento que está na posição 0 do s
#print(s[0][2]) 
#print(s[0][3]) 
#print(s[0][4]) # lembra que começa do 0 e vai até o 4

#----------------------------ou-----------------------------------

for c in s: # somente com três linhas de código eu consegui imprimir na tela todas as letras de minhas variáveis
    for x in c:
        print(x)
        #eu poderia colocar infinitas variáveis aqui