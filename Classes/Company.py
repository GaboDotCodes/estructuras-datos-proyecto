from Classes.Ship import Ship
from Classes.StorageTree import StorageTree

class Company:
  def __init__(self, name):
    self.name = name
    self.ships = [Ship('img/naves.png', 1), Ship('img/naves.png', 2), Ship('img/naves.png', 3)]
    self.storage = {
      "oro": 0,
      "plata": 0,
      "bronce": 0
    }
    self.storageTree = StorageTree()
  
  def getGatheringShips(self):
    filtered = filter(lambda ship: not ship.getAvailable(), self.ships)
    return list(filtered)
   
  def getAvailableShips(self):
    filtered = filter(lambda ship: ship.getAvailable(), self.ships)
    return list(filtered)
  
  def sendShipToGather(self, path):
    ships = self.getAvailableShips()
    if len(ships) >= 1:
      ship = ships[0]
      initial_x, initial_y, side = path[0].getX(), path[0].getY(), path[0].getSide()
      ship.setPath(path)
      ship.setAvailable(False)
      ship.setXPos(initial_x)
      ship.setYPos(initial_y)
      ship.setSide(side)
      ship.setActualPlanet(path[0])
    
  def receiveShipFromGather(self, ship):
    ship.setAvailable(True)