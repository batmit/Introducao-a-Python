#para separar uma string usamos split
s = "um tigre, dois tigres, três tigres"
print(s.split(",")) # eu vou separar a partir das vírgulas, usando elas como parâmetro
print(s.split()) # assim eu separo as palavras
# para separar uma string por linha usa:
m = """Uma linha
Duas Linhas
Três linhas"""
print(m.splitlines()) # splitliness, separar por linha

# no split colocamos algum valor para separar, ou deixamos vazio e assim separa as palavras
