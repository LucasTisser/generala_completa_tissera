import pygame
import sys
from modulos.logica_juego.juego_funciones import turno_jugadores
from modulos.interfaz.pygame_interface.core.assets import cargar_img_dados

from modulos.interfaz.pygame_interface.core.config import ANCHO
from modulos.interfaz.pygame_interface.ui.botones import dibujar_boton, crear_boton_tirar, dibujar_boton_icono, clickeado
from modulos.interfaz.pygame_interface.events.events import controlar_sonido

#from modulos.interfaz.pygame_interface.ui.textos import mostrar_texto
#from modulos.interfaz.pygame_interface.ui.dados import mostrar_dados, pedir_conservados_pygame
#from modulos.interfaz.pygame_interface.ui_pygame_jugadas import mostrar_menu_jugadas
#from modulos.interfaz.pygame_interface.screens.inicio_juego_orden import esperar_turno



def turno_jugadores_pygame(pantalla, fuente,fondo, hay_musica,boton_mute, icon_mute,icon_sonido, rondas, jugadores, categorias):
    # Wrappers gráficos

    imgs_dados = cargar_img_dados()

    def mostrar_texto(msg):
        # dibujar texto en pantalla
        pantalla.fill((0,0,0))  # limpiar
        texto_render = fuente.render(msg, True, (255,255,255))
        pantalla.blit(texto_render, (50, 50))
        pygame.display.flip()
        pygame.time.wait(1000)  # pausa breve para que se vea

    def esperar_turno(msg):
        mostrar_texto(msg)
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                    # Controlar mute dinámico
                    hay_musica = controlar_sonido(boton_mute, hay_musica)
                    esperando = False
        return hay_musica

    def mostrar_dados(dados):
        # dibujar imágenes de dados en pantalla
        x = 100
        for d in dados:
            imagen = imgs_dados[d]  # suponiendo que ya cargaste img_dados = cargar_img_dados()
            pantalla.blit(imagen, (x, 200))
            x += 70
        pygame.display.flip()

    def pedir_conservados(pantalla, dados, musica_activa, btn_mute, icon_sonido, icon_mute, btn_tirar):
        conservados = [False] * len(dados)
        esperando = True

        while esperando:
            rects_dados = mostrar_dados(pantalla, dados, conservados, ANCHO//2 - 250, 250)

            # botón mute
            if musica_activa:
                dibujar_boton_icono(pantalla, btn_mute, icon_sonido)
            else:
                dibujar_boton_icono(pantalla, btn_mute, icon_mute)

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

        return conservados, musica_activa
        #return []

    def pedir_categoria(tabla_puntajes, categorias, jugador):
        # interfaz para elegir categoría
        # placeholder: siempre la primera
        return {"nombre_cat": categorias[0]["Nombre"], "puntaje": tabla_puntajes[0]}

    def mostrar_tablero():
        # dibujar tablero de puntajes
        pass

    def obtener_puntos_jugadores():
        # devolver lista de puntajes actuales
        return [{"nombre": j["nombre"], "puntajeTotal": 0} for j in jugadores]

    def actualizar_tablero(jug_puntos):
        # actualizar estructura de puntajes
        pass


    # Llamada al bucle original con wrappers
    resultado = turno_jugadores(
        rondas,
        jugadores,
        categorias,
        mostrar_texto,
        esperar_turno,
        mostrar_dados,
        pedir_conservados,
        pedir_categoria,
        mostrar_tablero,
        obtener_puntos_jugadores,
        actualizar_tablero
    )

    return resultado

'''
def pantalla_juego(pantalla,
                    fuente,
                    fondo,
                    dados,
                    conservados,
                    tiros_restantes,
                    botones_jugadas,
                    jugador,
                    ronda_actual,
                    musica_activa,
                    btn_mute,
                    icon_sonido,
                    icon_mute,
                    tabla_puntajes):
    
    pantalla.blit(fondo, (0, 0))
    boton_tirar = crear_boton_tirar(fuente)

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

def bucle_juego(pantalla,fuente,fondo, jugadores_ordenados, musica_activa,boton_mute, icono_sonido, icono_mute, categorias):
    
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
        #lambda tabla, cats, jug: pedir_categoria_pygame(pantalla, tabla, cats, jug, musica_activa),

        # mostrar_tablero → dibujar tabla de puntajes
        #lambda: mostrar_tabla_puntajes(pantalla, fuente, obtener_puntos_jugadores(), 600, 150),

        #obtener_puntos_jugadores,
        #actualizar_tablero
    )

    # resultado contiene {"ganador": ..., "estadistica": ...}
    return resultado

'''