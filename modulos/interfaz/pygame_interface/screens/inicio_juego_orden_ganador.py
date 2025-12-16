import pygame
import sys
from modulos.interfaz.pygame_interface.core.assets import cargar_img_dados
from modulos.interfaz.pygame_interface.ui.botones import dibujar_boton_icono, clickeado
from modulos.interfaz.pygame_interface.core.utils import toggle_musica , manejar_hover

def mostrar_orden_final(pantalla, fuente, jugadores_ordenados, fondo, musica_act, btn_mute, icon_sonido, icon_mute, tamaño_dado=60):
    pantalla.blit(fondo, (0, 0))

    y = 150
    for i, j in enumerate(jugadores_ordenados, start=1):
        # texto centrado
        texto = fuente.render(f"{i}. {j['nombre']}", True, (255,255,255))
        x_texto = pantalla.get_width()//2 - (texto.get_width()//2 + tamaño_dado//2 + 10)
        pantalla.blit(texto, (x_texto, y))

        # dado al lado del nombre
        imagen = pygame.transform.scale(cargar_img_dados[j["dado"]], (tamaño_dado, tamaño_dado))
        x_dado = x_texto + texto.get_width() + 10
        pantalla.blit(imagen, (x_dado, y))

        y += tamaño_dado + 20

    # mostrar ganador
    ganador = jugadores_ordenados[0]
    mensaje_ganador = fuente.render(f"¡{ganador['nombre']} ganó la ronda y comienza primero!", True, (255,255,255))
    pantalla.blit(mensaje_ganador, (pantalla.get_width()//2 - mensaje_ganador.get_width()//2, y + 30))

    # texto de instrucción para continuar
    mensaje_continuar = fuente.render(
        "Presione una tecla o haga click para continuar...", True, (200,200,200)
    )
    pantalla.blit(
        mensaje_continuar,
        (pantalla.get_width()//2 - mensaje_continuar.get_width()//2, y + 80)
    )

    # botón mute
    if musica_act:
        dibujar_boton_icono(pantalla, btn_mute, icon_sonido)
    else:
        dibujar_boton_icono(pantalla, btn_mute, icon_mute)

    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return None, musica_act  # volver al menú
            elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                esperando = False  # cualquier tecla o clic avanza
            elif evento.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                manejar_hover([btn_mute], pos)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if clickeado(btn_mute, pos):
                    musica_act = toggle_musica(musica_act)
    return jugadores_ordenados, musica_act