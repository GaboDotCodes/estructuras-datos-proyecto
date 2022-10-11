from Classes.Tree.Node import *

class Planet(Node):
  def __init__(self, code, image, data):
    super().__init__(code, image, data)
  
  def produce(self):
    data = self.getData()['materials'].items()
    filtered = filter(lambda material: material[1] > 0, data)
    toUpdate = list(filtered)[0]
    self.updateData({'materials': { toUpdate[0]: toUpdate[1] + 2}})
    print(self.getData())