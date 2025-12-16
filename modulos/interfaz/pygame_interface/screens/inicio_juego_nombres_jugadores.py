import pygame
import sys

from modulos.interfaz.pygame_interface.core.utils import toggle_musica
from modulos.interfaz.pygame_interface.ui.botones import dibujar_boton_icono,clickeado

def ingresar_nombres(pantalla, fuente, cantidad, fondo,musica_act, btn_mute, icon_sonido, icon_mute):
    nombres = []
    input_activo = False
    for i in range(cantidad):
        texto = ""
        activo = True
        while activo:
            pantalla.blit(fondo, (0, 0))

            # Mensaje centrado
            mensaje = fuente.render(f"Ingrese nombre del jugador {i+1}:", True, (255,255,255))
            pantalla.blit(mensaje, (pantalla.get_width()//2 - mensaje.get_width()//2,150))

            # cuadro de texto
            rect_input = pygame.Rect(pantalla.get_width()//2 - 150, 250, 300, 50)
            pygame.draw.rect(pantalla, (255,255,255), rect_input)
            pygame.draw.rect(pantalla, (0,0,0), rect_input, 2)

            texto_render = fuente.render(texto, True, (0,0,0))
            pantalla.blit(texto_render, (rect_input.x+10, rect_input.y+10))

            # cursor titilante
            if input_activo:
                tiempo = pygame.time.get_ticks()
                if (tiempo // 500) % 2 == 0:  # alterna cada 500ms
                    cursor_x = rect_input.x + 10 + texto_render.get_width() + 2
                    cursor_y = rect_input.y + 5
                    pygame.draw.line(pantalla, (0,0,0), (cursor_x, cursor_y), (cursor_x, cursor_y + texto_render.get_height()))

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
                    return None, musica_act  # salir al menú
                elif evento.type == pygame.KEYDOWN:
                    if input_activo:
                        if evento.key == pygame.K_RETURN:
                            if texto.strip() != "":
                                nombres.append({"nombre": texto.strip()})
                                activo = False
                        elif evento.key == pygame.K_BACKSPACE:
                            texto = texto[:-1]
                        else:
                            texto += evento.unicode
                elif evento.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if btn_mute["rect"].collidepoint(pos):
                        if not btn_mute["hover"]:
                            btn_mute["hover"] = True
                            #sonido_hover.play()  # reproducir sonido al entrar
                    else:
                        btn_mute["hover"] = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if rect_input.collidepoint(pos):
                        input_activo = True  # activar cursor
                    else:
                        input_activo = False  # desactivar si clic fuera
                    if clickeado(btn_mute, pos):
                        musica_act = toggle_musica(musica_act)

    return nombres, musica_act