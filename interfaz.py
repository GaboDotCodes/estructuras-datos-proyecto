import pygame, sys
from Utils.generateGalacticSystemFromDict import *
from Utils.getJsonFromFile import *
from buttons import *
from load_img import *

#inicialización de pygame
pygame.init()

display = pygame.display.Info()
width = display.current_w
height = display.current_h
#creación del nombre, ícono, fondo y tamaño de la ventana 
window = pygame.display.set_mode((width, height - 50))
pygame.display.set_caption("Proyecto estructura de datos")
window.blit(pygame.image.load('img/bg1.jpg'), (0, 0))
pygame.display.set_icon(pygame.image.load('img/spaceship.png'))

#creación de datos de los botones con coordenadas y anchos 
generate_system = Rect(width - 250, 20, 200, 40)
pick_up = Rect(width - 250, 80, 200, 40)

#creación de botones en la pantalla
botones(window, generate_system, "Generate system")
botones(window, pick_up, "Gather")

# Imágenes en la pantalla 
load_img(window, pygame.image.load('img/store.png'), 10, 10)
load_img(window, pygame.image.load('img/naves.png'), 260, 10)
#ciclo de funcionamiento 
while True:
    #Salir del juego 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        # Si el mouse está sobre el botón 
        if event.type == MOUSEBUTTONDOWN:
            if pick_up.collidepoint(mouse.get_pos()):
                print("Clic")
            if generate_system.collidepoint(mouse.get_pos()):
                data = getJsonFromFile()
                galacticSystem = generateGalacticSystemFromDict(data)
                print(galacticSystem.show(galacticSystem.getFirstPlanet()))

    # actualizar cambios  
    pygame.display.update()
    pygame.display.flip()