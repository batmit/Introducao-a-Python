# para se remover espaços em branco usamos strip
t = "   Olá    "
print(t.strip()) # tirou todos os espaços vazios
print(t.rstrip()) # vai eliminar apenas os espaços vazios e direita

s = '...////Olá////...'
print(s.strip(".")) # você também pode remover o parâmetro entre parênteses, nesse caso vai remover os pontos
print(s.lstrip("."))
print(s.lstrip("./")) # vai remover os pontos e barras da esquerda