print("{0:05}".format(5)) # nesse caso vai ter o 0 preenchendo 5 espaços
print("{0:*=5}".format(32, 35)) # para usar algo diferente do 0 para preencher se deve usar =
print("{0:*^6}".format(32, 35)) # pego o número do format na posição 0, faço com que o * fique no meio para
# preencher um espaço de seis
print("{0:10,}".format(3247))
print("{0:10.5f}".format(3247.345))
print("{0:10,.5f}".format(3247.345))