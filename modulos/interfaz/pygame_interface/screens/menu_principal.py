import pygame
from modulos.interfaz.pygame_interface.core.config import ANCHO, BLANCO
from modulos.interfaz.pygame_interface.core.init import fuente_pygame, pantalla_pygame
from modulos.interfaz.pygame_interface.core.assets import cargar_fondo, blit_fondo,cargar_logo, cargar_icono_mute , cargar_icono_sonido
from modulos.interfaz.pygame_interface.ui.botones import crear_boton , dibujar_boton, dibujar_boton_icono, crear_boton_mute

from modulos.interfaz.pygame_interface.events.events import eventos_menu_principal

def menu_principal_pygame(pantalla, fuente, hay_musica):
    while True:
        fondo = cargar_fondo()
        blit_fondo(pantalla, fondo)
        botones_menu = []
        # Botones Menu Principal
        boton_jugar = crear_boton(ANCHO//2 - 100, 350, 220, 55, "Jugar", fuente, BLANCO)
        boton_estad = crear_boton(ANCHO//2 - 100, 420, 220, 55, "Estadísticas", fuente, BLANCO)
        boton_creditos = crear_boton(ANCHO//2 - 100, 490, 220, 55, "Créditos", fuente, BLANCO)
        boton_salir = crear_boton(ANCHO//2 - 100, 560, 220, 55, "Salir", fuente, BLANCO)

        botones_menu.append(boton_jugar)
        botones_menu.append(boton_estad)
        botones_menu.append(boton_creditos)
        botones_menu.append(boton_salir)

        boton_mute = crear_boton_mute(fuente)

        opciones = ["1) Jugar", "2) Estadísticas", "3) Créditos", "4) Salir"]

        dibujar_boton(pantalla, boton_jugar)
        dibujar_boton(pantalla, boton_estad)
        dibujar_boton(pantalla, boton_creditos)
        dibujar_boton(pantalla, boton_salir)

        dibujar_boton(pantalla, boton_mute)

        if hay_musica:
            dibujar_boton_icono(pantalla, boton_mute, cargar_icono_sonido(boton_mute))
        else:
            dibujar_boton_icono(pantalla, boton_mute, cargar_icono_mute(boton_mute))

        pygame.display.flip()

        eventos_menu_principal(pantalla, fuente, hay_musica , fondo, botones_menu, boton_mute, cargar_icono_sonido, cargar_icono_mute)
