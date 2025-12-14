import pygame

def mostrar_texto(pantalla, fuente, texto, x, y, color=(0,0,0)):
    render = fuente.render(texto, True, color)
    pantalla.blit(render, (x, y))