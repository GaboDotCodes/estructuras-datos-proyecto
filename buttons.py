from pygame import * 

def botones(window, boton, text):
    type_text = font.SysFont("Calibri", 18)
    boton.collidepoint(mouse.get_pos())
    draw.rect(window, (255, 0, 0), boton, 2)
    texto = type_text.render(text, True, (255, 255, 255))
    window.blit(texto, (boton.x+(boton.width-texto.get_width())/2, boton.y+(boton.height-texto.get_height())/2))


