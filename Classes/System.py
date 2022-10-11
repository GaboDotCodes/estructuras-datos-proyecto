from Classes.Company import Company
from Classes.GalacticSystem import GalacticSystem

class System:
  def __init__(self):
    self.galactic_system = GalacticSystem([('Name: ','name'), ('', 'materials')])
    self.company = Company("ACME")
    
  def getGalacticSystem(self):
    return self.galactic_system

  def getCompany(self):
    return self.company
  
  def gather(self):
    path = self.galactic_system.getRandomPathToNode()
    self.company.sendShipToGather(path)
    