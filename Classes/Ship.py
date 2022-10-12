from Classes.Planet import Planet

class Ship:
  def __init__(self, image, id):
    self.image = image
    self.id = id
    self.charge = None
    self.available = True
    self.path = []
    self.storage_x = 0
    self.storage_y = 0
    self.x_pos = 0
    self.y_pos = 0
    self.side = 0
    self.speed = 1
    self.actual_planet = None
    self.actual_index_in_points = 0
    self.list_of_points = []
  
  def getRoute(self):
    list_of_points = []
    
    before_point_x = self.storage_x
    before_point_y = self.storage_y
    
    actual_x = self.storage_x
    actual_y = self.storage_y
    
    list_of_points.append((actual_x, actual_y))
    for planet in self.path:
      next_point_x = planet.getX()
      next_point_y = planet.getY()
      
      step_x = next_point_x - before_point_x / 10000
      step_y = next_point_y - before_point_y / 10000
      for i in range(10000):
        actual_x = actual_x + step_x
        actual_y = actual_y + step_y
        list_of_points.append((actual_x, actual_y))
      before_point_x = next_point_x
      before_point_y = next_point_y
      
    return list_of_points
      
  def nextPlanet(self):
    last_index = len(self.path) - 1
    actual_index = self.path.index(self.actual_planet)
    if self.charge:
      return self.path[actual_index - 1] if actual_index != 0 else None
    return self.path[actual_index + 1] if actual_index != last_index else None
  
  def updatePosition(self):
    if self.actual_planet == None:
      self.setXPos(self.storage_x)
      self.setYPos(self.storage_y)
    else:
      self.setXPos(self.actual_planet.getX())
      self.setYPos(self.actual_planet.getY())
      self.actual_planet = self.nextPlanet()
  
  def updatePositionB(self):
    self.setXPos(self.list_of_points[self.actual_index_in_points][0])
    self.setYPos(self.list_of_points[self.actual_index_in_points][1])
    self.actual_index_in_points = self.actual_index_in_points + 1
    
  def updatePositionA(self, time):
    last_index = len(self.path) - 1
    actual_index = self.path.index(self.actual_planet)
    if self.nextPlanet():
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
    self.setXPos(self.storage_x)
    self.setYPos(self.storage_y)
    self.setXPos(self.getXPos() + 1)
    self.setYPos(self.getYPos() + 1)
    
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
    self.list_of_points = self.getRoute()
  
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