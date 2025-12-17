import pygame
import sys
from modulos.interfaz.pygame_interface.core.utils import toggle_musica , manejar_hover
from modulos.interfaz.pygame_interface.ui.botones import clickeado
from modulos.logica_juego.juego_funciones import cargar_categorias

def manejar_eventos_salida(evento):
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

def controlar_sonido(boton_mute, hay_musica):
    pos = pygame.mouse.get_pos()
    if clickeado(boton_mute, pos):
        #sonido_click.play()
        hay_musica = toggle_musica(hay_musica)
    return hay_musica

def eventos_menu_principal(pantalla, fuente, hay_musica, fondo, botones_menu, boton_mute, icon_sonido, icon_mute):
    accion = None 
    categorias = cargar_categorias()

    for evento in pygame.event.get():
        manejar_eventos_salida(evento)

        if evento.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            manejar_hover(botones_menu + [boton_mute], pos)

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Controlar sonido (mute/unmute)
            hay_musica = controlar_sonido(boton_mute,hay_musica)

            #Boton Jugar
            if clickeado(botones_menu[0], pos):
                accion = "jugar"
            # Boton Estadisticas 
            elif clickeado(botones_menu[1], pos):
                accion = "estadisticas"
            # Boton Creditos
            elif clickeado(botones_menu[2], pos):
                accion = "creditos"
            # Boton salir
            elif clickeado(botones_menu[3], pos):
                #sonido_click.play()
                pygame.quit()
                sys.exit()
    pygame.display.flip()
    return hay_musica, accion