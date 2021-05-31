def mdc(a, b):
     if b == 0:
         return a
     a = mdc(b, a % b)
     return a
print(mdc(120, 32))

def mmc(a, b):
    return abs(a * b) / mdc(a, b) # esse abs é o módulo
