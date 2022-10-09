class Company:
  def __init__(self, name, ships):
    self.name = name
    self.ships = ships
    self.storage = {
      "oro": 0,
      "plata": 0,
      "bronce": 0
    }
    self.storageTree = storageTree