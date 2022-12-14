from Classes.Planet import Planet

def getPlanetFromDict(dict):
  if (dict == None):
    return None
  planet = Planet(dict['name'], dict['materials'], dict['code'], dict['img'])
  planet.setLeftPlanet(getPlanetFromDict(dict['left']))
  planet.setRightPlanet(getPlanetFromDict(dict['right']))
  return planet
  