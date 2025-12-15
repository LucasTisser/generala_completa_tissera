import pygame
import sys
from modulos.config import OPCIONES_JUGADAS
from modulos.interfaz.pygame_interface.ui_pygame_botones import crear_boton, dibujar_boton, clickeado, dibujar_boton_icono
from modulos.interfaz.pygame_interface.ui_pygame_dados import mostrar_dados
from modulos.interfaz.pygame_interface.ui_pygame_jugadas import crear_botones_jugadas, mostrar_menu_jugadas, detectar_jugada_click
from modulos.logica_juego.juego_funciones import aplicar_conservados_y_tirar, puntajes_disponibles 
#from ui_pygame_textos import mostrar_texto
#from ui_pygame_tablero import mostrar_tablero
from modulos.interfaz.pygame_interface.ui_pygame_jugadores import seleccionar_cantidad_jugadores, ingresar_nombres
from modulos.interfaz.pygame_interface.ui_pygame_juego import decidir_orden_pygame


ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 200)

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Generala")
fuente = pygame.font.Font(None, 50)
musica_activa = True

fondo = pygame.image.load("assets/imagenes/fondo_menu.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

logo = pygame.image.load("assets/imagenes/logo_generala.png")
logo = pygame.transform.scale(logo, (300, 300))

# Botones del juego
boton_tirar = crear_boton(ANCHO//2 - 100, 600, 200, 50, "Tirar dados", fuente, BLANCO)

# BOTONES
boton_jugar = crear_boton(ANCHO//2 - 100, 350, 200, 50, "Jugar", fuente, BLANCO)
boton_estad = crear_boton(ANCHO//2 - 100, 420, 200, 50, "Estadísticas", fuente, BLANCO)
boton_creditos = crear_boton(ANCHO//2 - 100, 490, 200, 50, "Créditos", fuente, BLANCO)
boton_salir = crear_boton(ANCHO//2 - 100, 560, 200, 50, "Salir", fuente, BLANCO)

boton_mute = crear_boton(20, 20 , 60, 60, "", fuente, BLANCO)

sonido_click = pygame.mixer.Sound("assets/musica/sound_click.wav")

icono_sonido = pygame.image.load("assets/imagenes/icono_sonido.png")
icono_sonido = pygame.transform.scale(icono_sonido, (boton_mute["rect"].width - 10, boton_mute["rect"].height - 10))

icono_mute = pygame.image.load("assets/imagenes/icono_mute.png")
icono_mute = pygame.transform.scale(icono_mute, (boton_mute["rect"].width - 10, boton_mute["rect"].height - 10))

pygame.mixer.music.load("assets/musica/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.1)  # 30% del volumen
pygame.mixer.music.play(-1)

sonido_aves = pygame.mixer.Sound("assets/musica/sonido_fondo.mp3")
sonido_aves.set_volume(0.8)
sonido_aves.play(-1)  # -1 = loop infinito

dados = [1, 2, 3, 4, 5]
conservados = [False, False, False, False, False]
tiros_restantes = 3
botones_jugadas = crear_botones_jugadas(fuente, 50, 100, dados)

def mostrar_menu():
    opciones = ["1) Jugar", "2) Estadísticas", "3) Créditos", "4) Salir"]
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (ANCHO//2 - 150, 20))

    dibujar_boton(pantalla, boton_jugar)
    dibujar_boton(pantalla, boton_estad)
    dibujar_boton(pantalla, boton_creditos)
    dibujar_boton(pantalla, boton_salir)
    dibujar_boton(pantalla, boton_mute)

    if musica_activa:
        dibujar_boton_icono(pantalla, boton_mute, icono_sonido)
    else:
        dibujar_boton_icono(pantalla, boton_mute, icono_mute)

    pygame.display.flip()

def bucle_menu():
    global musica_activa
    while True:
        mostrar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for boton in [boton_jugar, boton_estad, boton_creditos, boton_salir, boton_mute]:
                    if boton["rect"].collidepoint(pos):
                        if not boton["hover"]:
                            boton["hover"] = True
                            #sonido_hover.play()  # reproducir sonido al entrar
                    else:
                        boton["hover"] = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()




                if clickeado(boton_jugar, pos):
                    sonido_click.play()


                    # Paso 1: elegir cantidad de jugadores
                    cantidad = seleccionar_cantidad_jugadores(pantalla, fuente, fondo)

                    # Paso 2: ingresar nombres
                    jugadores = ingresar_nombres(pantalla, fuente, cantidad, fondo)

                    # Paso 3: decidir orden
                    jugadores_ordenados = decidir_orden_pygame(pantalla, fuente, jugadores, fondo)

                    # Mostrar orden final en pantalla
                    pantalla.blit(fondo, (0, 0))
                    y = 150
                    for i, j in enumerate(jugadores_ordenados, start=1):
                        texto = fuente.render(f"{i}. {j['nombre']} (dado: {j['dado']})", True, (0,0,0))
                        pantalla.blit(texto, (200, y))
                        y += 50
                    pygame.display.flip()
                    pygame.time.wait(3000)


                    bucle_juego()

                elif clickeado(boton_estad, pos):
                    sonido_click.play()
                    print("Estadísticas")
                elif clickeado(boton_creditos, pos):
                    sonido_click.play()
                    print("Créditos")
                elif clickeado(boton_salir, pos):
                    sonido_click.play()
                    pygame.quit()
                    sys.exit()
                elif clickeado(boton_mute, pos):
                    sonido_click.play()
                    if musica_activa:
                        pygame.mixer.music.pause()
                        musica_activa = False
                        boton_mute["texto"] = fuente.render("", True, BLANCO)
                    else:
                        pygame.mixer.music.unpause()
                        musica_activa = True    
                        boton_mute["texto"] = fuente.render("", True, BLANCO)

def pantalla_juego(dados, conservados, tiros_restantes, botones_jugadas):
    pantalla.blit(fondo, (0, 0))
    #rects_dados = mostrar_dados(pantalla, dados, conservados, ANCHO//2 - 250, 250)

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
        dibujar_boton_icono(pantalla, boton_mute, icono_sonido)
    else:
        dibujar_boton_icono(pantalla, boton_mute, icono_mute)

    # Si ya no quedan tiros → mostrar menú de jugadas
    if tiros_restantes == 0:
        mostrar_menu_jugadas(pantalla, botones_jugadas)


    pygame.display.flip()
    return rects_dados

def bucle_juego():
    global musica_activa
    global tiros_restantes
    dados = [1, 2, 3, 4, 5]
    conservados = [False] * 5
    botones_jugadas = []

    while True:
        rects_dados = pantalla_juego(dados, conservados, tiros_restantes, botones_jugadas)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif evento.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for boton in [boton_jugar, boton_estad, boton_creditos, boton_salir, boton_mute]:
                    if boton["rect"].collidepoint(pos):
                        if not boton["hover"]:
                            boton["hover"] = True
                            #sonido_hover.play()  # reproducir sonido al entrar
                    else:
                        boton["hover"] = False
            
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Clic en botón tirar
                if clickeado(boton_tirar, pos) and tiros_restantes > 0:
                    sonido_click.play()
                    indices_conservados = [i for i, c in enumerate(conservados) if c]
                    dados = aplicar_conservados_y_tirar(dados, indices_conservados)
                    tiros_restantes -= 1

                # Clic en mute
                elif clickeado(boton_mute, pos):
                    sonido_click.play()
                    if musica_activa:
                        pygame.mixer.music.pause()
                        musica_activa = False
                    else:
                        pygame.mixer.music.unpause()
                        musica_activa = True

                # Clic en dado → alternar estado conservado (solo si quedan tiros)
                elif tiros_restantes > 0:
                    for i, rect in enumerate(rects_dados):
                        if rect.collidepoint(pos):
                            conservados[i] = not conservados[i]
                            sonido_click.play()
                
                # Selección de jugada (cuando ya no quedan tiros)
                
                # Clic en dado → alternar estado conservado
                elif tiros_restantes == 0:
                    # crear botones de jugadas con puntajes calculados
                    botones_jugadas = crear_botones_jugadas(fuente, 50, 100, dados, OPCIONES_JUGADAS)

                    # mostrar menú de jugadas
                    mostrar_menu_jugadas(pantalla, botones_jugadas)

                    # detectar clic en jugada
                    jugada = detectar_jugada_click(pos, botones_jugadas)
                    if jugada:
                        sonido_click.play()
                        print(f"Jugador eligió: {jugada['Nombre']}")
                        # Aquí después conectamos con la lógica para anotar en el tablero
                        # Resetear turno
                        tiros_restantes = 3
                        conservados = [False] * 5
                        dados = []

                
                else:
                    for i, rect in enumerate(rects_dados):
                        if rect.collidepoint(pos):
                            conservados[i] = not conservados[i]
                            sonido_click.play()

if __name__ == "__main__":
    bucle_menu()
