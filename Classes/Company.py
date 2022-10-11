from Classes.StorageTree import StorageTree


class Company:
  def __init__(self, name):
    self.name = name
    self.ships = None
    self.storage = {
      "oro": 0,
      "plata": 0,
      "bronce": 0
    }
    self.storageTree = StorageTree()