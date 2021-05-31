# eu também posso utilizar o método find e rfind com um começo e fim
s = 'um tigre, dois tigres, três tigres'
print(s.find("tigres"))
print(s.rfind("tigres"))
print(s.find("tigres", 7))# vai procurar o tigres a partir da posição 7
print(s.find("tigres", 30)) # vai dar um resultado negativo, isso porque não existe
print(s.find("tigres", 0, 10))# vai procurar tigres da posição 0 até a posição 10. resultado negativo novamente
print(s.find("tigre", 0, 10)) # aqui já achou. Não achou tigres, mas achou tigre
print(s.rfind("tigre", 0, 20)) # nesse caso vai pocurar a combinação tigre da direita para a esquerda de 0 a 20. Achou foi
# o segundo que tem tigre + s. 