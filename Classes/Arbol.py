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
    
    def Recorrido2(self, Padre):
        if Padre == None:
            return
        self.Recorrido2(Padre.getDer())
        self.lista2.append(Padre.getDato())
        self.Recorrido2(Padre.getIzq())

##get de las lista
    def getlista1(self):
        return self.lista1

    def getlista2(self):
        return self.lista2

    def EliminarH(self,Padre,dato):
        if Padre==None:
            return False
        if Padre.getDato()==dato:
            if Padre.getIzq()==None and Padre.getDer()==None: # es una hoja
                return True
        if dato<Padre.getDato():#avance por la izquierda
            if self.EliminarH(Padre.getIzq(),dato):
                Padre.setIzq(None)#Elimino por la izquierda
                return False
        if dato > Padre.getDato():  # avance por la derecha
            if self.EliminarH(Padre.getDer(), dato):
                Padre.setDer(None)#Elimino por la derecha
                return False
        return False

    def Eliminar1Hijo(self,Padre,dato):
        if Padre==None:
            return 0
        if Padre.getDato()==dato:
            if Padre.getIzq()!=None and Padre.getDer()==None:
                return 1
            if Padre.getIzq()==None and Padre.getDer()!=None:
                return 2

        if dato<Padre.getDato():# voy por la izquierda
            if self.Eliminar1Hijo(Padre.getIzq(),dato)==1:
                Padre.setIzq(Padre.getIzq().getIzq())
                return 0
            if self.Eliminar1Hijo(Padre.getIzq(), dato) == 2:
                Padre.setIzq(Padre.getIzq().getDer())
                return 0

        if dato>Padre.getDato():# voy por la derecha
            if self.Eliminar1Hijo(Padre.getDer(),dato)==1:
                Padre.setDer(Padre.getDer().getIzq())
                return 0
            if self.Eliminar1Hijo(Padre.getDer(), dato) == 2:
                Padre.setDer(Padre.getDer().getDer())
                return 0
        return 0

    def Eliminar2Hijos(self,Padre,dato):
        if Padre==None:
            return False

        if Padre.getDato()==dato:
            if Padre.getIzq()!=None and Padre.getDer()!=None:
                datop=self.Predecesor(Padre.getIzq())
                if self.EliminarH(Padre.getIzq(),datop):
                    Padre.setIzq(None)

                self.Eliminar1Hijo(Padre.getIzq(),datop)
                Padre.setDato(datop)
                return True

        if dato<Padre.getDato():
            if self.Eliminar2Hijos(Padre.getIzq(),dato):
                return False
        if dato>Padre.getDato():
            if self.Eliminar2Hijos(Padre.getDer(),dato) :
                return False
        return  False

    def Predecesor(self,Padre):
        if Padre.getDer()!=None:
            return(self.Predecesor(Padre.getDer()))
        else:
            return Padre.getDato()

    def Amplitud(self,dato):
        ListaA=[]
        ListaA.append(self.Raiz)
        i=0
        ListaDatos=[]

        while i<len(ListaA):
            Nodo=ListaA[i]
           # print("Amplitud {}".format(Nodo.getDato()))
            ListaA.pop(i)
            ListaDatos.append(Nodo)
            if Nodo.getIzq()!=None:
                ListaA.append(Nodo.getIzq())

            if Nodo.getDer() != None:
                ListaA.append(Nodo.getDer())

        self.Recorrerlista(ListaDatos,dato)

    def Recorrerlista(self,listadatos,dato):
        print(len(listadatos))
        for x in range(0, len(listadatos)):
            if listadatos[x].getDato()==dato:
                if listadatos[x].getDato()%2==0:
                    print("Puede Aterrirzar")
                else:
                    if listadatos[x+1].getDato()!=None:
                        if listadatos[x+1].getDato()%2==0:
                            print("Aterrizo donde su vecino: {}".format(listadatos[x+1].getDato()))
                        else:
                            print("Murio no pudo saltar al vecino: {}".format(listadatos[x+1].getDato()))
                    else:
                        print("No hay donde saltar murio")


    def Recorrido3(self,Padre):
        if Padre == None:
            return 0
        a=self.Recorrido3(Padre.getIzq())
        b=self.Recorrido3(Padre.getDer())
        return a+b+1

            