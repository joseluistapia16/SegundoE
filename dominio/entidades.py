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

# Codigo de Prueba
objC = Carro("NISSAN SENTRA","GMA005","NEGRO")
print(objC.getData())
objC.placa="AGM002"
objC.setModelo("TOYOTA TYRUS")
print(objC.getData())
print(objC.getModelo())