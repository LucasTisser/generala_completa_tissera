import pygame

from modulos.interfaz.pygame_interface.core.config import ANCHO, ALTO
# ----------------------------------------------------------
#                     I M A G E N E S
def cargar_fondo():
    fondo = pygame.image.load("assets/imagenes/fondo_menu.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    return fondo

def blit_fondo(pantalla, fondo):
    return pantalla.blit(fondo, (0, 0))

def cargar_logo():
    logo = pygame.image.load("assets/imagenes/logo_generala.png")
    logo = pygame.transform.scale(logo, (300, 300))

def cargar_img_dados():
    imagenes_dados = {
        1: pygame.image.load("assets/imagenes/1_dot.png"),
        2: pygame.image.load("assets/imagenes/2_dot.png"),
        3: pygame.image.load("assets/imagenes/3_dot.png"),
        4: pygame.image.load("assets/imagenes/4_dot.png"),
        5: pygame.image.load("assets/imagenes/5_dot.png"),
        6: pygame.image.load("assets/imagenes/6_dot.png"),
    }
    return imagenes_dados

def cargar_icono_sonido(boton_mute):
    icono_sonido = pygame.image.load("assets/imagenes/icono_sonido.png")
    icono_sonido = pygame.transform.scale(icono_sonido, (boton_mute["rect"].width - 10, boton_mute["rect"].height - 10))
    return icono_sonido

def cargar_icono_mute(boton_mute):
    icono = pygame.image.load("assets/imagenes/icono_mute.png")
    icono = pygame.transform.scale(icono, (boton_mute["rect"].width - 10, boton_mute["rect"].height - 10))
    return icono

# ----------------------------------------------------------
#                     S O N I D O S

def cargar_musica_fondo():
    pygame.mixer.music.load("assets/musica/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.1)  # 30% del volumen
    pygame.mixer.music.play(-1)

def cargar_musica_fondo_aves():
    sonido_aves = pygame.mixer.Sound("assets/musica/sonido_fondo.mp3")
    sonido_aves.set_volume(0.8)
    sonido_aves.play(-1)  # -1 = loop infinito

def cargar_sonido_click():
    sonido_click = pygame.mixer.Sound("assets/musica/sound_click.wav")
    return sonido_click



