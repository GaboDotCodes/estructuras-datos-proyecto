class Node:
    def __init__(self, code, image, data):
        self.code = code
        self.image = image
        self.data = data
        self.left = None
        self.right = None
        self.visited = False

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
    
    def updateData(self, dataToUpdate):
     self.data.update(dataToUpdate)
    
    def setLeft(self, left):
        self.left=left
    
    def setRight(self, right):
        self.right = right
    
    def visit(self):
        self.visited = True
        
    def isLeaf(self):
        return self.left == None and self.right == None
