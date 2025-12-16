import pygame
import sys
from modulos.logica_juego.juego_funciones import decidir_orden

from modulos.interfaz.pygame_interface.ui.botones import crear_boton,dibujar_boton, dibujar_boton_icono, clickeado
from modulos.interfaz.pygame_interface.core.utils import toggle_musica, manejar_hover
from modulos.interfaz.pygame_interface.ui.textos import mostrar_texto
from modulos.interfaz.pygame_interface.ui.dados import mostrar_dado_unico

def esperar_turno(pantalla, fuente, mensaje, fondo, musica_act, btn_mute, icon_sonido, icon_mute):
    ancho_pantalla = pantalla.get_width()
    alto_pantalla = pantalla.get_height()
    
    boton_tirar = crear_boton(ancho_pantalla//2 - 100, alto_pantalla//2, 200, 60, "Tirar dado", fuente)
    while True:
        pantalla.blit(fondo, (0, 0))

        texto_render = fuente.render(mensaje, True, (255,255,255))
        pantalla.blit(
            texto_render, 
            (ancho_pantalla//2 - texto_render.get_width()//2,
            alto_pantalla//2 - 100)
        )
        
        dibujar_boton(pantalla, boton_tirar)

        # dibujar botón mute
        if musica_act:
            dibujar_boton_icono(pantalla, btn_mute, icon_sonido)
        else:
            dibujar_boton_icono(pantalla, btn_mute, icon_mute)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                manejar_hover([boton_tirar, btn_mute], pos)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if clickeado(boton_tirar, pos):
                    #sonido_click.play()
                    return True, musica_act  # jugador tiró el dado
                if clickeado(btn_mute, pos):
                    musica_act = toggle_musica(musica_act)

def decidir_orden_pygame(pantalla, fuente, jugadores, fondo, musica_act, btn_mute, icon_sonido, icon_mute):
    return decidir_orden(
        jugadores,
        lambda msg: mostrar_texto(pantalla, fuente, msg, fondo),
        lambda msg: esperar_turno(pantalla, fuente, msg, fondo, musica_act, btn_mute, icon_sonido, icon_mute),
        lambda dados: mostrar_dado_unico(pantalla, fondo, dados[0], musica_act, btn_mute, icon_sonido, icon_mute)
    )