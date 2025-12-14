import pygame

def crear_boton(x, y, ancho, alto, texto, fuente, color_fondo, color_texto):
    return {
        "rect": pygame.Rect(x, y, ancho, alto),
        "texto": fuente.render(texto, True, color_texto),
        "color_fondo": color_fondo
    }

def dibujar_boton(pantalla, boton):
    pygame.draw.rect(pantalla, boton["color_fondo"], boton["rect"])
    pantalla.blit(boton["texto"], (boton["rect"].x + 10, boton["rect"].y + 10))

def clickeado(boton, pos_mouse):
    return boton["rect"].collidepoint(pos_mouse)
