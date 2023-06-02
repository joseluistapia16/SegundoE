class Carro:

    def __init__(self,modelo, placa,color):
        self.__modelo = modelo
        self.placa = placa
        self.color = color
        print(self.__getPrivado("Daliana"))

    def setModelo(self,modelo):
        self.__modelo=modelo

    def getModelo(self):
        return self.__modelo

    def getData(self):
        return self.__modelo+" "+self.placa+" "+self.color
    def __getPrivado(self,nombre):
        return "Hola "+nombre
class Metodos:

    def __init__(self,valor):
        self._valor = valor

    def imprimir(self,nombre):
        return "Hola "+nombre

class Persona:

    def __init__(self,cedula, nombre,direccion):
        self.__cedula = cedula
        self.nombre = nombre
        self.direccion = direccion

    def setCedula(self,cedula):
        self.__cedula= cedula

    def getCedula(self):
        return self.__cedula

    def getData(self):
        return self.__cedula+" "+self.nombre+" "+self.direccion

    def getFields(self):
        return  None

class Proveedor(Persona):

    def __init__(self,cedula,nombre,direccion,codigo):
        Persona.__init__(self,cedula,nombre,direccion)
        self.codigo = codigo

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+self.direccion+" "+self.codigo

class Cliente(Persona,Metodos):

    def __init__(self,cedula, nombre, direccion,cod_cli):
        Persona.__init__(self,cedula,nombre,direccion)
        self.codigo = cod_cli

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+self.direccion+" "+self.codigo

    def imprimir(self,nombre):
        print("Segundo E")
        self._valor = nombre
        return "Hola "+self._valor

    def getFields(self):
        return "Cedula:"+self.getCedula()+"\nNombre:"+self.nombre+\
            "\nDireccion:"+self.direccion+"\nCodigo:"+self.codigo
class Producto:

    def __init__(self,codigo,nombre,categoria):
        self.__codigo= codigo
        self.nombre = nombre
        self.categoria = categoria

    def setCodigo(self,codigo):
        self.__codigo= codigo

    def getCodigo(self):
        return self.__codigo


# Codigo de Prueba
""" 
objC = Carro("NISSAN SENTRA","GMA005","NEGRO")
print(objC.getData())
objC.placa="AGM002"
objC.setModelo("TOYOTA TYRUS")
print(objC.getData())
print(objC.getModelo())

objP = Proveedor("098765","GORKY QUIÑONEZ","LA PUNTILLA","PR001")
print(objP.getData())
objP.setCedula("94747455")
print(objP.getData())
objCl = Cliente("09977","KARLA CANALES","SAMBORONDON","CL001")
print(objCl.getData())
objCl.nombre="KARLA POATAN"
objCl.setCedula("058577")
print(objCl.getData())
print(objCl.imprimir("EZEQUIEL"))
"""
