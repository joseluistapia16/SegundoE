from dominio.entidades import *
from menus.menuE import *
from procesos.data import *
from archivos.archivos import *
class Run:

    def __init__(self):
        self.ruta  = "C:/Users/Usuario/PycharmProjects/SegundoE/segundoE.csv"
        self.men = MenuE()
        self.lista = []
        self.proc = Process()
        self.arch = Archivo()

    def start(self):
        opc = ("REGISTRO","CONSULTA","ACTUALIZAR",
               "ELIMINAR","LISTAR", "SALIR")
        op = self.men.getMenu(opc)
        if op== 1:
            self.__registro()
            self.start()
        if op==2:
            self.__consulta()
            self.start()

        if op==3:
            self.__actualizar()
            self.start()
        if op==4:
            self.__eliminar()
            self.start()
        if op== 5:
            self.__listar()
            self.start()


    def __registro(self):
        print("\t\tRegistro de Clientes")
        cedula = input("Cedula:")
        self.lista= self.arch.getClients(self.ruta)
        pos = self.proc.getClientPos(self.lista,cedula)
        if pos==-1:
            nombre = input("Nombre:")
            direccion = input("Direccion:")
            codigo = input("Codigo:")
            obj = Cliente(cedula,nombre,direccion,codigo)
            msg = obj.getCedula()+";"+obj.nombre+";"+obj.direccion+";"+obj.codigo+";\n"
            self.arch.create(self.ruta,msg,"a")
        else:
            print("Cedula ya existe!!")
        input("<Enter> para continuar...")


    def __listar(self):
        print("\t\tLISTADO DE ESTUDIANTES")
        self.lista= self.arch.getClients(self.ruta)
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Enter> para continuar...")

    def __consulta(self):
        print("\t\tCONSULTA DE CLIENTES")
        ced = input("Cedula:")
        self.lista= self.arch.getClients(self.ruta)
        obj = self.proc.getClient(self.lista,ced)
        if obj !=None:
            print(obj.getFields())
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")

    def __actualizar(self):
        print("\t\tACTUALIZAR DATOS DE CLIENTES")
        ced = input("Cedula:")
        self.lista = self.arch.getClients(self.ruta)
        pos = self.proc.getClientPos(self.lista,ced)
        if pos>-1:
            print(self.lista[pos].getFields())
            nombre = input("Nombre:")
            direccion = input("Direccion:")
            codigo = input("Codigo:")
            self.lista[pos].nombre = nombre
            self.lista[pos].direccion= direccion
            self.lista[pos].codigo = codigo
            msg = ""
            for i in range(len(self.lista)):
                msg= msg+self.lista[i].getCedula()+";"+\
                     self.lista[i].nombre+";"+self.lista[i].direccion+";"+\
                                             self.lista[i].codigo+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Datos actualizados!")
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")

    def __eliminar(self):
        print("\t\tELIMINAR DATOS DE CLIENTES")
        ced = input("Cedula:")
        self.lista= self.arch.getClients(self.ruta)
        pos = self.proc.getClientPos(self.lista,ced)
        if pos>-1:
            print(self.lista[pos].getFields())
            input("Datos a eliminar....")
            self.lista.pop(pos)
            msg = ""
            for i in range(len(self.lista)):
                msg = msg+ self.lista[i].getCedula()+";"+self.lista[i].nombre+";"+\
                      self.lista[i].direccion+";"+self.lista[i].codigo+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Datos borrados")
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")



    """

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
    """



