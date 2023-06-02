from dominio.entidades import *
class Archivo:

    def create(self,ruta,datos,modo):
        arch = open(ruta,modo)
        arch.write(datos)
        arch.close()

    def getClients(self,ruta):
        lista = []
        try:
            arch = open(ruta,"r")
            for linea in arch.readlines():
                tupla = linea.split(";")
                obj = Cliente(tupla[0],tupla[1],tupla[2],tupla[3])
                lista.append(obj)
            arch.close()
        except:
            print("Archivo vacio..")
        return lista