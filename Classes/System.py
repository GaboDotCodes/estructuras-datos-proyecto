from Classes.GalacticSystem import GalacticSystem

class System:
  def __init__(self):
    self.galactic_system = GalacticSystem([('Name: ','name'), ('', 'materials')])
    self.company = None
  
  def setGalacticSystem(self, galactic_system):
    self.galactic_system = galactic_system
    
  def getGalacticSystem(self):
    return self.galactic_system
  
  def setGalacticSystem(self, galacticSystem):
    self.galactic_system = galacticSystem
  
  def setCompany(self, company):
    self.company = company