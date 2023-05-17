def suma(x,y):
    r =(x+y)
    return r
def getPromedio(x,y,z):
    return ((x+ y + z) / 3)

def getMessage(pr):
    if pr< 0 or pr>10:
        return "Valor invalido!"
    else:
        if pr<7 and pr>=0:
            return "REPROBADO"
        if pr>=7 and pr<=10:
            return "APROBADO"

def getAge(edad):
    if edad<0 or edad>120:
        return "Edad incorrecta!"
    else:
        if edad>=0 and edad<11:
            return "Infantes!"
        if edad>10 and edad<18:
            return "Adolescente!"
        if edad>17 and edad<26:
            return "Joven"
        if edad>25 and edad<65:
            return "Adulto!"
    if edad>64:
        return "Adulto mayor!"