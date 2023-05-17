from procesos.operaciones import *
from procesos.data import *
from menus.menuE import *
def funcion2():
    print("Segundo E")
    v2 = 56
    v1 = 'Poatan'
    v3 = str(v2)+v1
    print(v3)

def funcion3():
    n1 = float(input("Numero 1:"))
    n2 = float(input("Numero 2:"))
    r= suma(n1,n2)
    print("Total:"+str(r))

def funcion4():
    edad = int(input("edad:"))
    msg = getAge(edad)
    print(msg)
def funcion5():
    c=0
    while c<5:
        c= c+1
        print(c)
    c=0
    ac = 0
    while c<10:
        c= c+1
        if c % 2!=0:
            ac= ac + c
            print(c)
    print("Total acumulado:"+str(ac))

    c=0
    ac =0
    for i in range(1,11):
        if i % 2==0:
            c= c+1
            ac = ac +i
            print(i)
    print("Total de pares "+str(c))
    print("Acumulados "+str(ac))

def funcion6():
    tupla1 = (34,True,"jose",23.90,False)
    print(tupla1)
    tupla1=(90,7)
    print(tupla1)
    for i in range(len(tupla1)):
        print(tupla1[i])
    lista = []
    lista.append(56)
    lista.append(65)
    lista.append("Jose")
    lista.append(True)
    print(lista)
    lista[1]=100
    print(lista)
    #lista.pop(1)
    del lista[1]
    print(lista)
    for i in range(len(lista)):
        print(lista[i])

    datos = {
        "clave1" :  40,
        False : "2E",
        (3,True,78): True
    }
    datos[False]="POO"
    datos[56]=390
    del datos["clave1"]
    print(datos)

def funcion7():
    nombre = input("Nombre:")
    materia = input("Materia:")
    n1 = inputFloat("Nota 1:")
    n2 = inputFloat("Nota 2:")
    n3 = inputFloat("Nota 3:")
    pr = getPromedio(n1,n2,n3)
    msg = getMessage(pr)
    if msg!="Valor invalido!":
        print("El promedio es:" + str(pr))
    print(msg)

def funcion8():
    tupla=("Registro","Consulta","Actualizar",
           "Eliminar","Listar","Salir")
    opc =getMenu(tupla)
    if opc == 1:
        print("Python")
        input("<Enter> para continuar...")
        funcion8()
    if opc==2:
        print("Java")
    if opc==3:
        print("C#")

def funcion9():
    lista = []
    c =0
    while c<5:
        nombre = input("Nombre "+str(c+1)+":")
        r1 = getRepeat(lista,nombre)
        if r1==False:
           lista.append(nombre)
        else:
            c= c -1
        c= c +1

    for i in range(len(lista)):
        print(lista[i])

def funcion1():
    print("Hola mundo")
    print("POO")

funcion9()






