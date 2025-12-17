import pygame
from modulos.interfaz.pygame_interface.core.config import ANCHO, BLANCO
from modulos.interfaz.pygame_interface.core.assets import cargar_fondo, blit_fondo, cargar_logo, blit_logo, cargar_icono_mute , cargar_icono_sonido
from modulos.interfaz.pygame_interface.ui.botones import crear_boton , dibujar_boton, dibujar_boton_icono, crear_boton_mute
from modulos.interfaz.pygame_interface.events.events import eventos_menu_principal
from modulos.interfaz.pygame_interface.screens.inicio_juego import principio_juego_pygame
from modulos.interfaz.pygame_interface.screens.bucle_juego import turno_jugadores_pygame
from modulos.logica_juego.juego_funciones import cargar_categorias


def menu_principal_pygame(pantalla, fuente, hay_musica):
    fondo = cargar_fondo()
    logo = cargar_logo()
    # Botones Menu Principal
    boton_jugar = crear_boton(ANCHO//2 - 110, 350, 220, 55, "Jugar", fuente, BLANCO)
    boton_estad = crear_boton(ANCHO//2 - 110, 420, 220, 55, "Estadísticas", fuente, BLANCO)
    boton_creditos = crear_boton(ANCHO//2 - 110, 490, 220, 55, "Créditos", fuente, BLANCO)
    boton_salir = crear_boton(ANCHO//2 - 110, 560, 220, 55, "Salir", fuente, BLANCO)

    botones_menu = [boton_jugar,boton_estad,boton_creditos,boton_salir]

    boton_mute = crear_boton_mute(fuente)

    icono_sonido = cargar_icono_sonido(boton_mute)
    icono_mute = cargar_icono_mute(boton_mute)
    
    while True:
        blit_fondo(pantalla, fondo)
        blit_logo(pantalla, logo)

        dibujar_boton(pantalla, boton_jugar)
        dibujar_boton(pantalla, boton_estad)
        dibujar_boton(pantalla, boton_creditos)
        dibujar_boton(pantalla, boton_salir)

        dibujar_boton(pantalla, boton_mute)

        if hay_musica:
            dibujar_boton_icono(pantalla, boton_mute, icono_sonido)
        else:
            dibujar_boton_icono(pantalla, boton_mute, icono_mute)

        pygame.display.flip()

        hay_musica, accion = eventos_menu_principal(pantalla, fuente, hay_musica , fondo, botones_menu, boton_mute, icono_sonido, icono_mute)

        if accion == "jugar":
            rondas = 1
            categorias = cargar_categorias()
            lista_jug_ordenada = principio_juego_pygame(pantalla,fuente, fondo,hay_musica, boton_mute,icono_sonido, icono_mute)
            print(lista_jug_ordenada)
            for i in range(2):
                rondas += 1
                ganador_y_est = turno_jugadores_pygame(
                pantalla,
                fuente,
                fondo,
                hay_musica,
                boton_mute,
                icono_mute,
                icono_sonido,
                rondas,
                lista_jug_ordenada,
                categorias)
        
        elif accion == "estadisticas":
            #sonido_click.play()
            print("Estadísticas")
            #mostrar_estadisticas(...)
        elif accion == "creditos":
            #sonido_click.play()
            print("Créditos")
            #mostrar_creditos(...)