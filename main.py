import pygame, sys, threading
from time import sleep
from Classes.Planet import Planet
from Classes.System import *
from Classes.Button import *
from Utils.getJsonFromFile import *
from load_img import *

# Inicialización de pygame
pygame.init()

display = pygame.display.Info()
width = display.current_w
height = display.current_h

# Creación del nombre, ícono, fondo y tamaño de la ventana 
window = pygame.display.set_mode((width, height - 50))
pygame.display.set_caption("Proyecto estructura de datos")
pygame.display.set_icon(pygame.image.load('img/spaceship.png'))

generalSystem = System()

generateSystemBtn = Button(window, Rect(width - 250, 20, 200, 40), "Generate system")
gatherBtn = Button(window, Rect(width - 250, 80, 200, 40), "Gather")

galacticSystemRect = Rect(width * 0.3, height * 0.2, width * 0.65, height * 0.70)
storageTreeRect = Rect(width * 0.025, height * 0.2, width * 0.25, height * 0.70)

producing = False
def produce():
    while True:
        if producing:
            break
        sleep(10)
        generalSystem.getGalacticSystem().produce()
        pygame.display.update()
    
produce_thread = threading.Thread(target=produce, args=())

# Ciclo de funcionamiento 
while True:
    window.blit(pygame.image.load('img/bg1.jpg'), (0, 0))
    # Imágenes en la pantalla 
    load_img(window, pygame.image.load('img/store.png'), 10, 10)
    load_img(window, pygame.image.load('img/naves.png'), 260, 10)
    generateSystemBtn.show()
    gatherBtn.show()

    # Salir del juego 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            producing = True
            sys.exit()
        
        # Si el mouse está sobre el botón 
        if event.type == MOUSEBUTTONDOWN:
            if gatherBtn.getCP(mouse.get_pos()):
                print("Clic")
            if generateSystemBtn.getCP(mouse.get_pos()):
                data = getJsonFromFile()
                for planet in data['planets']:
                    newPlanet = Planet(planet['code'], planet['image'], planet['data'])
                    generalSystem.getGalacticSystem().addNode(newPlanet)
                produce_thread.start()
    generalSystem.getGalacticSystem().showTree(window, galacticSystemRect)
    
    # Actualizar cambios
    pygame.display.update()