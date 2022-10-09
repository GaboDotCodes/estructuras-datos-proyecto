class GalacticSystem:
  def __init__(self, firstPlanet):
    self.firstPlanet = firstPlanet
  
  def getFirstPlanet(self):
    return self.firstPlanet
  
  def show(self, temp):
    if temp == None:
      return ''
    return self.show(temp.getLeftPlanet()) + ' - ' + temp.getName() + ' - ' + self.show(temp.getRightPlanet())
  
  