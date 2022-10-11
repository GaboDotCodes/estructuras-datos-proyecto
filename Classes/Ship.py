from Classes.Planet import Planet


class Ship:
  def __init__(self, image, id):
    self.image = image
    self.id = id
    self.charge = None
    self.available = True
    self.path = []
    self.x_pos = 0
    self.y_pos = 0
    self.side = 0
    self.speed = 1
    self.actual_planet = None
  
  def nextPlanet(self):
    last_index = len(self.path) - 1
    actual_index = self.path.index(self.actual_planet)
    if self.charge:
      return self.path[actual_index - 1] if actual_index != 0 else None
    return self.path[actual_index + 1] if actual_index != last_index else None
    
  def updatePosition(self, time):
    last_index = len(self.path) - 1
    actual_index = self.path.index(self.actual_planet)
    if self.getXPos() == self.nextPlanet().getX() and self.getYPos() == self.nextPlanet().getY():
      if actual_index == last_index:
        self.extractMaterial(self.actual_planet)
      self.setActualPlanet(self.nextPlanet())
      
    leftDistanceX = self.nextPlanet().getX() - self.actual_planet.getX()
    leftDistanceY = self.nextPlanet().getY() - self.actual_planet.getY()
    
    leftTimeX = leftDistanceX / self.speed
    leftTimeY = leftDistanceY / self.speed
    
    stepX = leftDistanceX / (leftTimeX / time / 1000)
    stepY = leftDistanceY / (leftTimeY / time / 1000)
    
    nextXPos = self.getXPos() + leftDistanceX if stepX > leftDistanceX else stepX
    nextYPos = self.getYPos() + leftDistanceY if stepY > leftDistanceY else stepY
    
    self.setXPos(nextXPos)
    self.setYPos(nextYPos)
    
  def getImage(self):
    return self.image
  
  def getId(self):
    return self.id
  
  def getPath(self):
    return self.path
  
  def getXPos(self):
    return self.x_pos
  
  def getYPos(self):
    return self.y_pos
    
  def getSide(self):
    return self.side
    
  def getSpeed(self):
    return self.speed
  
  def getActualPlanet(self):
    return self.actual_planet
  
  def getAvailable(self):
    return self.available
  
  def setAvailable(self, available):
    self.available = available
    
  def setPath(self, path):
    self.path = path
  
  def setXPos(self, x_pos):
    self.x_pos = x_pos
  
  def setYPos(self, y_pos):
    self.y_pos = y_pos
    
  def setSide(self, side):
    self.side = side
  
  def setActualPlanet(self, actual_planet):
    self.actual_planet = actual_planet
  
  def extractMaterial(self, planet):
    result = planet.extractMaterial(30)
    if result['result']:
      self.charge = result['materials']