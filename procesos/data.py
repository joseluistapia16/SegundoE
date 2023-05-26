class Inputs:
    def inputFloat(self,msg):
        valor =-1
        while valor<0 or valor>10:
            try:
                valor= float(input(msg))
            except:
                print("valor incorrecto!")
                valor=-1
        return valor

    def inputInt(self,msg):
        valor =-1
        while valor<0 or valor>10:
            try:
                valor= int(input(msg))
            except:
                print("valor incorrecto!")
                valor=-1
        return valor

    def getRepeat(self,lista,valor):
        res = False
        for i in range(len(lista)):
            if valor== lista[i]:
                res = True
                break
        return res
