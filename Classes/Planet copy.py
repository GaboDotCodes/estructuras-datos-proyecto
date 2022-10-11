class Planet:
  def __init__(self, name, materials, code, image):
    self.name = name
    self.materials = materials
    self.code = code
    self.image = image
    self.leftPlanet = None
    self.rightPlanet = None
    
  def __getitem__(self, arg):
        return str(arg)*3

  def getName(self):
    return self.name
  
  def getMaterials(self):
    return self.materials
  
  def getMaterial(self, material):
    return self.materials[material]
  
  def getCode(self):
    return self.code
  
  def getRightPlanet(self):
    return self.rightPlanet

  def getLeftPlanet(self):
    return self.leftPlanet
  
  def setRightPlanet(self, rightPlanet):
    self.rightPlanet = rightPlanet

  def setLeftPlanet(self, leftPlanet):
    self.leftPlanet = leftPlanet

  def extractMaterial(self, material, amount):
    if (self.materials[material] < amount):
      raise ValueError("Material is not enough")
    self.materials[material] = self.materials[material] - amount