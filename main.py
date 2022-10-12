import traceback
import pygame, sys, threading
from time import sleep
from Classes.Planet import Planet
from Classes.System import *
from Classes.Button import *
from Utils.getJsonFromFile import *
from load_img import *

# Inicialización de pygame
pygame.init()

clock = pygame.time.Clock()

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

producing = True
def produce():
    while True:
        if not producing:
            break
        sleep(10)
        generalSystem.getGalacticSystem().produce()
    
produce_thread = threading.Thread(target=produce, args=())

gathering = True
def gather():
    while True:
        if not producing:
            break
        generalSystem.gather()
        sleep(5)
    
gather_thread = threading.Thread(target=gather, args=())


moving_ships = True
def move_ships():
    while True:
        if not moving_ships:
            break
        for ship in generalSystem.getCompany().getGatheringShips():
            print('ID: {} LEN: {}'.format(ship.getId(), len(ship.getPath())))
            ship_image = ship.getImage()
            side = ship.getSide()
            img = pygame.image.load(ship_image)
            img_t = transform.scale(img, (side, side))
            load_img(window, img_t, ship.getXPos(), ship.getYPos())
            ship.updatePosition()
        sleep(2)
    
moving_ships_thread = threading.Thread(target=move_ships, args=())

running = True

# Ciclo de funcionamiento 
try:
    while running:
        window.blit(pygame.image.load('img/bg1.jpg'), (0, 0))
        # Imágenes en la pantalla 
        load_img(window, pygame.image.load('img/store.png'), 10, 10)
        load_img(window, pygame.image.load('img/naves.png'), 260, 10)
        generateSystemBtn.show()
        gatherBtn.show()

        # Salir del juego 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                producing = False
                gathering = False
                running = False
                moving_ships = False
                sys.exit()
            
            # Si el mouse está sobre el botón 
            if event.type == MOUSEBUTTONDOWN:
                if gatherBtn.getCP(mouse.get_pos()):
                    if generalSystem.getGalacticSystem().getRoot() == None:
                        print('No se puede recoletar sin un sistema')
                    elif not gather_thread.is_alive():
                        gather_thread.start()
                        moving_ships_thread.start()
                    
                if generateSystemBtn.getCP(mouse.get_pos()):
                    data = getJsonFromFile()
                    for planet in data['planets']:
                        newPlanet = Planet(planet['code'], planet['image'], planet['data'])
                        generalSystem.getGalacticSystem().addNode(newPlanet)
                    produce_thread.start()
        
        generalSystem.getGalacticSystem().showTree(window, galacticSystemRect)
        
        # for ship in generalSystem.getCompany().getGatheringShips():
        #     print('ID: {} LEN: {}'.format(ship.getId(), len(ship.getPath())))
        #     ship_image = ship.getImage()
        #     side = ship.getSide()
        #     img = pygame.image.load(ship_image)
        #     img_t = transform.scale(img, (side, side))
        #     load_img(window, img_t, ship.getXPos(), ship.getYPos())
        #     ship.updatePosition()
        
        clock.tick(30)
        # Actualizar cambios
        pygame.display.update()
        
    pygame.quit()
except Exception:
    traceback.print_exc()
    pygame.quit()
    sys.exit(1)