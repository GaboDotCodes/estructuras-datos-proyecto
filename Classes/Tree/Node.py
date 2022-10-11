class Node:
    def __init__(self, code, image, data):
        self.code = code
        self.image = image
        self.data = data
        self.left = None
        self.right = None
        self.x = 0
        self.y = 0
        self.side = 0

    def getCode(self):
        return self.code
    
    def getImage(self):
        return self.image
    
    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getSide(self):
        return self.side
    
    def updateData(self, dataToUpdate):
     self.data.update(dataToUpdate)
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
    
    def setSide(self, side):
        self.side = side
    
    def setLeft(self, left):
        self.left=left
    
    def setRight(self, right):
        self.right = right
        
    def isLeaf(self):
        return self.left == None and self.right == None