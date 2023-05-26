from dominio.entidades import *
from menus.menuE import *
class Run:

    def __init__(self):
        self.men = MenuE()
        self.lista = []

    def start(self):
        opc = ("REGISTRO","CONSULTA","ACTUALIZAR",
               "ELIMINAR","LISTAR", "SALIR")
        op = self.men.getMenu(opc)
        if op== 1:
            self.__registro()
            self.start()

        if op== 5:
            self.__listar()
            self.start()


    def __registro(self):
        print("\t\tRegistro de Clientes")
        cedula = input("Cedula:")
        nombre = input("Nombre:")
        direccion = input("Direccion:")
        codigo = input("Codigo:")
        obj = Cliente(cedula,nombre,direccion,codigo)
        self.lista.append(obj)
        input("<Enter> para continuar...")


    def __listar(self):
        print("\t\tLISTADO DE ESTUDIANTES")
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Enter> para continuar...")

    def prueba(self):
        lista = []
        objCl1 = Cliente("09977", "KARLA CANALES", "SAMBORONDON", "CL001")
        objCl2 = Cliente("02334", "ELIZABETH GONZALEZ", "GUASMO", "CL002")
        objCl3 = Cliente("12345", "CARLOS MERINO", "SUBURBIO", "CL003")
        objCl4 = Cliente("74848", "MALENA MIÑO", "CRISTO DEL CONSUELO", "CL004")
        objCl5 = Cliente("11223", "JOSE MEDINA", "FLOR DE BASTION", "CL005")
        lista.append(objCl1)
        lista.append(objCl2)
        lista.append(objCl3)
        lista.append(objCl4)
        lista.append(objCl5)
        for i in range(len(lista)):
            print(lista[i].getData())

        cedula = input("Cedula:")
        obj = self.getClient(lista, cedula)
        if obj == None:
            print("Cedula no existe!")
        else:
            print(obj.getData())

    def getClient(self,lista, cedula):
        obj = None
        for i in range(len(lista)):
            if cedula == lista[i].getCedula():
                obj = lista[i]
                break
        return obj

