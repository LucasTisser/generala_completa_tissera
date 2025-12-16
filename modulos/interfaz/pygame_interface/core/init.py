import pygame
from modulos.interfaz.pygame_interface.core.config import ANCHO, ALTO

def init_pygame():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Generala")

def pantalla_pygame():
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    return pantalla

def fuente_pygame():
    fuente = pygame.font.Font(None, 50)
    return fuente

def clock_pygame():
    clock = pygame.time.Clock()
    return clock
    
def musica_activa_pygame():
    musica_activa = True
    return musica_activa
