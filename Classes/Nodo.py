class Nodo:
    def __init__(self, dato):
        self.dato = dato 
        self.Izq = None 
        self.Der = None 

    def getdato(self):
        return self.dato

    def getIzq(self):
        return self.Izq

    def getDer(self):
        return self.Der

    def setdato(self, dato):
        self.dato = dato
    
    def setIzq(self, Izq):
        self.Izq=Izq
    
    def setDer(self, Der):
        self.Der = Der
