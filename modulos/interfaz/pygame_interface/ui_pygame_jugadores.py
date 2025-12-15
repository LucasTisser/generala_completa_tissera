import pygame
import sys
from modulos.interfaz.pygame_interface.ui_pygame_botones import crear_boton, dibujar_boton, clickeado, dibujar_boton_icono


def seleccionar_cantidad_jugadores(pantalla, fuente, fondo):
    botones = [
        crear_boton(200, 200, 500, 100, "2 jugadores", fuente),
        crear_boton(200, 300, 500, 100, "3 jugadores", fuente),
        crear_boton(200, 400, 500, 100, "4 jugadores", fuente),
    ]

    while True:
        pantalla.blit(fondo, (0, 0))
        for boton in botones:
            dibujar_boton(pantalla, boton)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i, boton in enumerate(botones, start=2):
                    if clickeado(boton, pos):
                        #sonido_click.play()
                        return i  # devuelve 2, 3 o 4


def ingresar_nombres(pantalla, fuente, cantidad, fondo):
    nombres = []
    for i in range(cantidad):
        texto = ""
        activo = True
        while activo:
            pantalla.blit(fondo, (0, 0))
            mensaje = fuente.render(f"Ingrese nombre del jugador {i+1}:", True, (0,0,0))
            pantalla.blit(mensaje, (200, 150))

            # cuadro de texto
            rect_input = pygame.Rect(200, 250, 300, 50)
            pygame.draw.rect(pantalla, (255,255,255), rect_input)
            pygame.draw.rect(pantalla, (0,0,0), rect_input, 2)

            texto_render = fuente.render(texto, True, (0,0,0))
            pantalla.blit(texto_render, (rect_input.x+10, rect_input.y+10))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if texto.strip() != "":
                            nombres.append({"nombre": texto.strip()})
                            activo = False
                    elif evento.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    else:
                        texto += evento.unicode
    return nombres
