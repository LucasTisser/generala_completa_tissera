import pygame
import sys
from modulos.interfaz.pygame_interface.ui.botones import crear_boton, dibujar_boton, dibujar_boton_icono, clickeado , crear_boton_mute , crear_boton_tirar
from modulos.interfaz.pygame_interface.core.utils import toggle_musica, manejar_hover

def seleccionar_cantidad_jugadores(pantalla, fuente, fondo, musica_act, btn_mute, icon_sonido, icon_mute):
    ancho_pantalla = pantalla.get_width()
    x_centrado = ancho_pantalla // 2 - 150

    btn_2jug = crear_boton(x_centrado, 200, 300, 70, "2 jugadores", fuente)
    btn_3jug = crear_boton(x_centrado, 300, 300, 70, "3 jugadores", fuente)
    btn_4jug = crear_boton(x_centrado, 400, 300, 70, "4 jugadores", fuente)
    boton_mute = btn_mute

    while True:
        pantalla.blit(fondo, (0, 0))

        # título
        titulo = fuente.render("Seleccione el número de jugadores : ", True, (255,255,255))
        pantalla.blit(titulo, (ancho_pantalla//2 - titulo.get_width()//2, 100))

        for boton in [btn_2jug, btn_3jug, btn_4jug]:
            dibujar_boton(pantalla, boton)
        
        if musica_act:
            dibujar_boton_icono(pantalla, btn_mute, icon_sonido)
        else:
            dibujar_boton_icono(pantalla, btn_mute, icon_mute)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return None, musica_act
            elif evento.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                manejar_hover([btn_2jug, btn_3jug, btn_4jug, boton_mute], pos)
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                pos = pygame.mouse.get_pos()

                if clickeado(btn_mute, pos):
                    #sonido_click.play()
                    musica_act = toggle_musica(musica_act)
                    continue
                for i, boton in enumerate([btn_2jug, btn_3jug, btn_4jug], start=2):
                    if clickeado(boton, pos):
                        #sonido_click.play()
                        return i, musica_act  # devuelve 2, 3 o 4