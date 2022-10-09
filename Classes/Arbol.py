class Arbol:
    def __init__(self):
        self.Raiz= None
        self.lista1= []

    def getRaiz(self):
        return self.Raiz
    
    def agregar(self, Nuevo):
        if self.Raiz == None:
            self.Raiz = Nuevo
        else:
            self.agregarABB(self.Raiz, Nuevo)
    
    def agregarABB(self, temp, Nuevo):
        if temp == None: 
            return True
        
        if Nuevo.getdato()> temp.getdato(): #realiza el recorrido por la derecha 
            if self.agregarABB(temp.getDer(), Nuevo):
                temp.setDer(Nuevo)

        if Nuevo.getdato()< temp.getdato(): #realiza el recorrido por la izquierda 
            if self.agregarABB(temp.getIzq(), Nuevo):
                temp.setIzq(Nuevo)

    def getlista1(self):
        return self.lista1

    def Recorrido1(self, padre):
        if padre == None:
            return
        
        self.Recorrido1(padre.getIzq())
        self.lista1.append(padre.getdato())
        self.Recorrido1(padre.getDer())
    