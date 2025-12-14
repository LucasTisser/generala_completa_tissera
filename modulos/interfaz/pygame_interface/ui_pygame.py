import pygame
import sys
from ui_pygame_textos import mostrar_texto
from ui_pygame_botones import crear_boton, dibujar_boton, clickeado
#from modulos.interfaz.pygame.ui_pygame_dados import mostrar_dados
#from modulos.interfaz.pygame.ui_pygame_tablero import mostrar_tablero

ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 200)

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Generala")
fuente = pygame.font.Font(None, 50)

fondo = pygame.image.load("../../../assets/imagenes/fondo_menu.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

logo = pygame.image.load("../../../assets/imagenes/logo_generala.png")
logo = pygame.transform.scale(logo, (300, 300))

pygame.mixer.music.load("../../../assets/musica/sonido_fondo.mp3")
pygame.mixer.music.play(-1)  # -1 = loop infinito

# BOTONES
boton_jugar = crear_boton(ANCHO//2 - 100, 200, 200, 50, "Jugar", fuente, AZUL, BLANCO)
boton_estad = crear_boton(ANCHO//2 - 100, 270, 200, 50, "Estadísticas", fuente, AZUL, BLANCO)
boton_creditos = crear_boton(ANCHO//2 - 100, 340, 200, 50, "Créditos", fuente, AZUL, BLANCO)
boton_salir = crear_boton(ANCHO//2 - 100, 410, 200, 50, "Salir", fuente, AZUL, BLANCO)

def mostrar_menu():
    opciones = ["1) Jugar", "2) Estadísticas", "3) Créditos", "4) Salir"]
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (ANCHO//2 - 150, 20))

    dibujar_boton(pantalla, boton_jugar)
    dibujar_boton(pantalla, boton_estad)
    dibujar_boton(pantalla, boton_creditos)
    dibujar_boton(pantalla, boton_salir)

    pygame.display.flip()

def bucle_menu():
    while True:
        mostrar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if clickeado(boton_jugar, pos):
                    print("Jugar")
                elif clickeado(boton_estad, pos):
                    print("Estadísticas")
                elif clickeado(boton_creditos, pos):
                    print("Créditos")
                elif clickeado(boton_salir, pos):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    bucle_menu()
