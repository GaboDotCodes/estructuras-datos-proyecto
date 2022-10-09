from Classes.GalacticSystem import GalacticSystem
from Utils.getPlanetFromDict import getPlanetFromDict

def generateGalacticSystemFromDict(dict):
  firstPlanet = getPlanetFromDict(dict['firstPlanet'])
  galacticSystem = GalacticSystem(firstPlanet)
  return galacticSystem