def verificação(string, max, min):
    if len(string) > min and len(string) < max:
        return f"A string {string} está correta!"
    else:
        return f"Está errado, tente novamente"
print(verificação("batata", 10, 3))