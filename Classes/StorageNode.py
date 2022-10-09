class StorageNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    pass
  
  def __getitem__(self, arg):
        return str(arg)*3
  
  def setLeft(self, left):
    self.left = left
    
  def setRight(self, right):
    self.right = right
  
  def getData(self):
    return self.data
    
  def getLeft(self):
    return self.left
  
  def getRight(self):
    return self.right