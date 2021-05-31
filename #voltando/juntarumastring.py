a = "batata"
b = "assada"
s = list(a)
s.extend(b)
print(s)
# no append eu adiciono algum valor para a lista, nesse caso eu preciso usar extend

s = "".join(s)
print(s) # juntou tudo

#primeiro eu faço uma lista com os valores de a. Depois dou um extend adicionando os valores de b
#então uso a função "".join(s), para juntar os valores. Fica uma string misturada