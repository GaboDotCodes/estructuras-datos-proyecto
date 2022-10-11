from Classes.Tree.Node import *

class Planet(Node):
  def __init__(self, code, image, data):
    super().__init__(code, image, data)
    self.visited = False
  
  def visit(self):
    self.visited = True
        
  def extractMaterial(self, amount):
    data = self.getData()['materials'].items()
    filtered = filter(lambda material: material[1] > 0, data)
    toUpdate = list(filtered)[0]
    if toUpdate[1] == 0:
      print('Material insuficiente')
      return { 'result': False, 'materials' : None }
    newAmount = toUpdate[1] - amount if amount >= toUpdate[1] else 0
    self.updateData({'materials' : { toUpdate[0]: newAmount}})
    self.visit()
    return { 'result' : True, 'materials' : { toUpdate[0]: toUpdate[1] - newAmount } }
    
  def produce(self):
    data = self.getData()['materials'].items()
    filtered = filter(lambda material: material[1] > 0, data)
    toUpdate = list(filtered)[0]
    self.updateData({'materials': { toUpdate[0]: toUpdate[1] + 2}})