#strings são imutáveis no python
#podemos, entretanto, mudar uma lista que contém strings
L = list("AlôMundo") # l recebe o valor dentro transformado em lista
L[0] = "a" # vai substituir o primeiro valor e deixa-lo negativo
print(L)

s = ''.join(L) # une os valres da lista e forma novamente uma string
#join parece ser uma variável que precisa receber um valor antes, por isso as aspas vazias. Não pode
#colocar só .join(), tem que ter um valor antes
print(s) # já quando fica como uma string eu não posso mudar mais o valor