from Classes.Tree.Tree import Tree

class GalacticSystem(Tree):
  def __init__(self, toShow):
    super().__init__(toShow)
    
  def produce(self):
    if self.getRoot() == None:
      return None
    self.produceInPlanets(self.getRoot())
    
  def produceInPlanets(self, planet):
    planet.produce()
    if planet.getLeft() != None:
      self.produceInPlanets(planet.getLeft())
    if planet.getRight() != None:
      self.produceInPlanets(planet.getRight())