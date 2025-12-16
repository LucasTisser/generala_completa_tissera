import pygame
from modulos.interfaz.pygame_interface.core.config import ANCHO , BLANCO

def crear_boton(x, y, ancho, alto, texto, fuente, color_texto=(255,255,255)):
    return {
        "rect": pygame.Rect(x, y, ancho, alto),
        "texto": fuente.render(texto, True, color_texto),
        "hover": False
    }

def dibujar_boton(pantalla, boton):
    rect = boton["rect"]
    texto = boton["texto"]

    if boton.get("hover", False):
        # Hover → borde blanco
        pygame.draw.rect(pantalla, (255, 255, 255), rect,  5, border_radius=10)
    else:
        # Normal → fondo transparente (solo borde negro)
        pygame.draw.rect(pantalla, (0, 0, 0), rect, 5, border_radius=10)

    # Centrar el texto dentro del rectángulo
    texto_rect = texto.get_rect(center=rect.center)
    pantalla.blit(texto, texto_rect)

def clickeado(boton, pos_mouse):
    return boton["rect"].collidepoint(pos_mouse)

def dibujar_boton_icono(pantalla, boton, icono):
    if boton.get("hover", False):
        # Hover →, borde blanco
        pygame.draw.rect(pantalla, (255, 255, 255), boton["rect"],  5, border_radius=10)
    else:
        # Normal → fondo transparente (solo borde negro)
        pygame.draw.rect(pantalla, (0, 0, 0), boton["rect"], 5, border_radius=10)

    pantalla.blit(icono, (boton["rect"].x + 5, boton["rect"].y + 5))

# ---------------------------------------------------------------------------------------
#                           B O T O N E S


def crear_boton_tirar(fuente):
    boton_tirar = crear_boton(ANCHO//2 - 100, 600, 200, 50, "Tirar dados", fuente, BLANCO)

def crear_boton_mute(fuente):
    return crear_boton(20, 20 , 70, 70, "", fuente, BLANCO)
