import pygame
#import sys
#from modulos.interfaz.pygame_interface.core.config import categorias_lista
#from modulos.interfaz.pygame_interface.ui.dados import mostrar_dados, mostrar_orden_final
#from modulos.interfaz.pygame_interface.ui_pygame_jugadas import crear_botones_jugadas, mostrar_menu_jugadas
#from modulos.logica_juego.juego_funciones import turno_jugadores ,aplicar_conservados_y_tirar, puntajes_disponibles 
#from modulos.interfaz.pygame_interface.ui.textos import mostrar_texto
#from ui_pygame_tablero import mostrar_tablero
#from modulos.interfaz.pygame_interface.screens.inicio_juego_cant_jugadores import seleccionar_cantidad_jugadores
#from modulos.interfaz.pygame_interface.screens.inicio_juego_nombres_jugadores import ingresar_nombres
#from modulos.interfaz.pygame_interface.screens.inicio_juego_orden import decidir_orden_pygame
#from modulos.interfaz.pygame_interface.core.utils import toggle_musica , manejar_hover



# ------- NUEVO ---------
from modulos.interfaz.pygame_interface.core.init import init_pygame, pantalla_pygame,fuente_pygame,clock_pygame,musica_activa_pygame
#from modulos.interfaz.pygame_interface.core.assets import cargar_fondo
#from modulos.interfaz.pygame_interface.ui.botones import dibujar_boton, clickeado, dibujar_boton_icono
from modulos.interfaz.pygame_interface.screens.menu_principal import menu_principal_pygame

dados = [1, 2, 3, 4, 5]
conservados = [False, False, False, False, False]
tiros_restantes = 3




#botones_jugadas = crear_botones_jugadas(fuente, 50, 100, dados)




def main():
    init_pygame()
    pantalla = pantalla_pygame()
    fuente = fuente_pygame()
    clock = clock_pygame()
    musica_activa = musica_activa_pygame()


    menu_principal_pygame(pantalla, fuente, musica_activa)


'''
def pantalla_juego(dados, conservados, tiros_restantes, botones_jugadas, jugador, ronda_actual, musica_activa, btn_mute, icon_sonido, icon_mute, tabla_puntajes):
    pantalla.blit(fondo, (0, 0))

    # título con ronda
    titulo = fuente.render(f"Ronda {ronda_actual}", True, (255,255,255))
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 20))

    # turno del jugador
    turno_texto = fuente.render(f"Turno de {jugador['nombre']}", True, (255,255,255))
    pantalla.blit(turno_texto, (ANCHO//2 - turno_texto.get_width()//2, 70))

    rects_dados = []
    if tiros_restantes < 3:
        rects_dados = mostrar_dados(pantalla, dados, conservados, ANCHO//2 - 250, 250)

    # Botón tirar (solo si quedan tiros)
    if tiros_restantes > 0:
        dibujar_boton(pantalla, boton_tirar)



    # Ejemplo: tablero (cuando lo tengas implementado)
    # mostrar_tablero(pantalla, tablero, 900, 100)




    # Botón tirar
    #dibujar_boton(pantalla, boton_tirar)

    # Botón mute/unmute
    if musica_activa:
        dibujar_boton_icono(pantalla, btn_mute, icon_sonido)
    else:
        dibujar_boton_icono(pantalla, btn_mute, icon_mute)

    # Si ya no quedan tiros → mostrar menú de jugadas
    if tiros_restantes == 0:
        mostrar_menu_jugadas(pantalla, botones_jugadas)

    # tabla de puntuaciones
    #mostrar_tabla_puntajes(pantalla, fuente, tabla_puntajes, 600, 150)

    pygame.display.flip()
    return rects_dados
'''

'''
def bucle_juego(jugadores_ordenados, musica_activa, categorias):
    rondas = 1  # o el número máximo de rondas que quieras
    resultado = turno_jugadores(
        rondas,
        jugadores_ordenados,
        categorias,

        # === Wrappers gráficos ===
        lambda msg: mostrar_texto(pantalla, fuente, msg, fondo),
        lambda msg: esperar_turno(pantalla, fuente, msg, fondo, musica_activa, boton_mute, icono_sonido, icono_mute),
        lambda dados: mostrar_dados(pantalla, dados, [False]*len(dados), ANCHO//2 - 250, 250),

        # pedir_conservados → acá usás clic en los dados
        lambda dados: pedir_conservados_pygame(pantalla, dados, musica_activa),

        # pedir_categoria → menú de jugadas
        lambda tabla, cats, jug: pedir_categoria_pygame(pantalla, tabla, cats, jug, musica_activa),

        # mostrar_tablero → dibujar tabla de puntajes
        lambda: mostrar_tabla_puntajes(pantalla, fuente, obtener_puntos_jugadores(), 600, 150),

        obtener_puntos_jugadores,
        actualizar_tablero
    )

    # resultado contiene {"ganador": ..., "estadistica": ...}
    return resultado
'''

if __name__ == "__main__":
    main()
