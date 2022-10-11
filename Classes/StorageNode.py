class StorageNode:
    def __init__(self, code, material):
        self.code = code
        self.material = material
        self.left = None
        self.right = None

    def getCode(self):
        return self.code

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    
    def setLeft(self, left):
        self.left=left
    
    def setRight(self, right):
        self.right = right
