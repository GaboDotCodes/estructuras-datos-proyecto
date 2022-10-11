class StorageTree:
    def __init__(self):
        self.root = None
        self.list = []

    def getRoot(self):
        return self.root
    
    def addNode(self, Node):
        if self.root == None:
            self.root = Node
        else:
            self.add(self.root, Node)
    
    def add(self, temp, Node):
        if temp == None: 
            return True
        
        if Node.getCode()> temp.getCode(): # Realiza el recorrido por la derecha 
            if self.add(temp.getRight(), Node):
                temp.setRight(Node)

        if Node.getCode()< temp.getCode(): # Realiza el recorrido por la izquierda 
            if self.add(temp.getLeft(), Node):
                temp.setLeft(Node)

    def getList(self):
        return self.list

    def Recorrido1(self, padre):
        if padre == None:
            return
        
        self.Recorrido1(padre.getIzq())
        self.list.append(padre.getdato())
        self.Recorrido1(padre.getDer())
    