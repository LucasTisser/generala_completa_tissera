import pygame
import sys

from modulos.interfaz.pygame_interface.ui.botones import dibujar_boton, dibujar_boton_icono, clickeado , crear_boton_mute , crear_boton_tirar
from modulos.interfaz.pygame_interface.core.utils import toggle_musica, manejar_hover
from modulos.interfaz.pygame_interface.core.assets import cargar_img_dados, cargar_icono_mute , cargar_icono_sonido
from modulos.interfaz.pygame_interface.core.config import ANCHO

def mostrar_dado_unico(pantalla, fondo, valor, musica_act, btn_mute, icon_sonido, icon_mute, tamaño=100, duracion=1000):
    inicio = pygame.time.get_ticks()

    while pygame.time.get_ticks() - inicio < duracion:
        pantalla.blit(fondo, (0, 0))

        # centrar dado
        x = pantalla.get_width()//2 - tamaño//2
        y = pantalla.get_height()//2  # debajo del título y botón
        imagen = pygame.transform.scale(cargar_img_dados[valor], (tamaño, tamaño))
        rect = pygame.Rect(x, y, tamaño, tamaño)
        pantalla.blit(imagen, rect.topleft)

        # borde negro
        pygame.draw.rect(pantalla, (0,0,0), rect, 2, border_radius=10)

        # botón mute
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
                    manejar_hover([btn_mute], pos)
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if clickeado(btn_mute, pos):
                        musica_act = toggle_musica(musica_act)
    return True, musica_act

def mostrar_dados(pantalla, dados, conservados, x, y, tamaño=100):
    rects = []
    for i, valor in enumerate(dados):
        imagen = pygame.transform.scale(cargar_img_dados[valor], (tamaño, tamaño))
        rect = pygame.Rect(x + i*(tamaño+20), y, tamaño, tamaño)
        pantalla.blit(imagen, rect.topleft)

        # Si el dado está conservado → dibujar borde rojo
        if conservados[i]:
            pygame.draw.rect(pantalla, (200,0,0), rect, 4)
        else:
            pygame.draw.rect(pantalla, (0,0,0), rect, 2)

        rects.append(rect)
    return rects

def pedir_conservados_pygame(pantalla, dados, musica_activa):
    conservados = [False] * len(dados)
    esperando = True

    while esperando:
        rects_dados = mostrar_dados(pantalla, dados, conservados, ANCHO//2 - 250, 250)

        # botón mute
        if musica_activa:
            dibujar_boton_icono(pantalla, crear_boton_mute, cargar_icono_sonido)
        else:
            dibujar_boton_icono(pantalla, crear_boton_mute, cargar_icono_mute)

        dibujar_boton(pantalla, crear_boton_tirar)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return None  # volver al menú
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # clic en dado → alternar estado
                for i, rect in enumerate(rects_dados):
                    if rect.collidepoint(pos):
                        conservados[i] = not conservados[i]
                        #sonido_click.play()
                # clic en tirar → confirmar selección
                if clickeado(crear_boton_tirar, pos):
                    #sonido_click.play()
                    esperando = False

    return conservados
