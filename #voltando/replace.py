# para substituir uma string usamos o comando replace
# com o replace usamos duas strings, a que queremos substituir e então por qual queremos
s = "um tigre, dois tigres, três tigres"
print(s.split(",")) # vou separar por vírgula
print(s.replace("tigre", "gato")) # como você vê, acabou substituindo todos os três gatos
# podemos apenas substituir 1 deles colocando o 1 no lugar
print(s.replace("tigre", "gato", 1))# vai substituir com o replace o tigre, colocar o gato apenas 1 vez
# o replace de fato facilita e muito e não tenho que fazer uma estrutura de repetição gigantesca
print(s.replace(",", "-"))

print(s.replace('',"batata")) # vai colocar batata antes de todos os caracteres, todos
print(s.replace("tigre", None)) # vai substituir por um valor nulo, ou seja, vai apagar tudo, não só tigre
# vai apagar a frase inteira