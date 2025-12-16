import pygame
import sys

from modulos.interfaz.pygame_interface.core.utils import toggle_musica , manejar_hover
from modulos.interfaz.pygame_interface.ui.botones import clickeado
from modulos.interfaz.pygame_interface.screens.inicio_juego_cant_jugadores import seleccionar_cantidad_jugadores
from modulos.interfaz.pygame_interface.screens.inicio_juego_nombres_jugadores import ingresar_nombres
from modulos.interfaz.pygame_interface.screens.inicio_juego_orden import decidir_orden_pygame
from modulos.interfaz.pygame_interface.screens.inicio_juego_orden_ganador import mostrar_orden_final


def manejar_eventos_salida(evento):
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

def controlar_sonido(boton_mute):
    pos = pygame.mouse.get_pos()
    if clickeado(boton_mute, pos):
        #sonido_click.play()
        musica_activa = toggle_musica(musica_activa)
    return musica_activa

def eventos_menu_principal(pantalla, fuente, hay_musica, fondo, botones_menu, boton_mute, icon_sonido, icon_mute):
    for evento in pygame.event.get():
        manejar_eventos_salida(evento)
        if evento.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            #manejar_hover([botones_menu, boton_mute], pos)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if clickeado(botones_menu[0], pos):
                #sonido_click.play()
                # Paso 1: elegir cantidad de jugadores
                cantidad, hay_musica = seleccionar_cantidad_jugadores(pantalla, fuente, fondo, hay_musica, boton_mute , icon_sonido , icon_mute)
                if cantidad is None:
                    # volver al menú principal sin romper
                    continue
                # Paso 2: ingresar nombres
                jugadores, hay_musica = ingresar_nombres(pantalla, fuente, cantidad, fondo, hay_musica, boton_mute, icon_sonido, icon_mute)
                if jugadores is None:
                    # volver al menú principal sin romper
                    continue
                # Paso 3: decidir orden
                jugadores_ordenados = decidir_orden_pygame(pantalla, fuente, jugadores, fondo, hay_musica, boton_mute, icon_sonido, icon_mute)
                # mostrar orden final
                mostrar_orden_final(pantalla, fuente, jugadores_ordenados, fondo, hay_musica, boton_mute, icon_sonido, icon_mute)
                pygame.display.flip()



            elif clickeado(botones_menu[1], pos):
                #sonido_click.play()
                print("Estadísticas")
            elif clickeado(botones_menu[2], pos):
                #sonido_click.play()
                print("Créditos")
            elif clickeado(botones_menu[3], pos):
                #sonido_click.play()
                pygame.quit()
                sys.exit()