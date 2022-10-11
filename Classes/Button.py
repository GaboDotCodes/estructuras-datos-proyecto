from pygame import *

class Button:
  def __init__(self, window, rect, text) -> None:
    self.window = window
    self.rect = rect
    self.text = text
  
  def getCP(self, point):
    return self.rect.collidepoint(point)
  
  def show(self):
    draw.rect(self.window, (255, 0, 0), self.rect, 2)
    texto = font.SysFont("Calibri", 18).render(self.text, True, (255, 255, 255))
    self.window.blit(texto, (self.rect.x+(self.rect.width-texto.get_width())/2, self.rect.y+(self.rect.height-texto.get_height())/2))