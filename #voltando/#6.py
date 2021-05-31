s = 'um tigre, dois tigres, três tigres'
p = 0
while p > -1: # enquanto o p for verdadeiro:
    p = s.find("tigre", p )# tem que ir aumentando para não pegar sempre o mesmo valor
    if p >= 0: # vou retornar alguma coisa somente se o valor for positivo
        print(f"Posição: {p}")
        p += 1
# o p recebe a posição de início, depois eu vou procurar a partir dessa posição