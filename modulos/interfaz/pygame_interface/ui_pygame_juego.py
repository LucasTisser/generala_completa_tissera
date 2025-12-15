import pygame
import sys
#from modulos.logica_juego.juego_funciones import turno_jugadores, cargar_categorias
from modulos.interfaz.pygame_interface.ui_pygame_botones import crear_boton, dibujar_boton, clickeado, dibujar_boton_icono
from modulos.interfaz.pygame_interface.ui_pygame_dados import mostrar_dados
from modulos.logica_juego.juego_funciones import decidir_orden


def mostrar_texto(pantalla, fuente, mensaje, fondo):
    pantalla.blit(fondo, (0, 0))
    texto_render = fuente.render(mensaje, True, (0,0,0))
    pantalla.blit(texto_render, (100, 100))
    pygame.display.flip()

def esperar_turno(pantalla, fuente, mensaje,fondo):
    boton_tirar = crear_boton(200, 300, 200, 60, "Tirar dado", fuente)
    while True:
        pantalla.blit(fondo, (0, 0))
        texto_render = fuente.render(mensaje, True, (0,0,0))
        pantalla.blit(texto_render, (100, 150))
        dibujar_boton(pantalla, boton_tirar)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if clickeado(boton_tirar, pos):
                    #sonido_click.play()
                    return  # sale cuando el jugador clickea

def mostrar_dados(pantalla, fuente, valores, fondo):
    pantalla.blit(fondo, (0, 0))
    mensaje = fuente.render(f"Dado: {valores[0]}", True, (0,0,0))
    pantalla.blit(mensaje, (200, 200))
    pygame.display.flip()
    pygame.time.wait(1000)  # pausa breve para que se vea

def decidir_orden_pygame(pantalla, fuente, jugadores, fondo):
    return decidir_orden(
        jugadores,
        lambda msg: mostrar_texto(pantalla, fuente, msg, fondo),
        lambda msg: esperar_turno(pantalla, fuente, msg, fondo),
        lambda dados: mostrar_dados(pantalla, fuente, dados, fondo)
    )