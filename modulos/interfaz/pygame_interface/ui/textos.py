import pygame

def mostrar_texto(pantalla, fuente, mensaje, fondo):
    pantalla.blit(fondo, (0, 0))
    texto_render = fuente.render(mensaje, True, (0,0,0))
    pantalla.blit(texto_render, (100, 100))
    pygame.display.flip()