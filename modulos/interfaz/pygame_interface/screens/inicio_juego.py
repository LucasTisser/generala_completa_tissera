from modulos.interfaz.pygame_interface.screens.inicio_juego_cant_jugadores import seleccionar_cantidad_jugadores
from modulos.interfaz.pygame_interface.screens.inicio_juego_nombres_jugadores import ingresar_nombres
from modulos.interfaz.pygame_interface.screens.inicio_juego_orden import decidir_orden_pygame
from modulos.interfaz.pygame_interface.screens.inicio_juego_orden_ganador import mostrar_orden_final
from modulos.datos.datos_funciones import construir_jugadores, guardar_jugadores, creacion_tablero

url_jugadores = "./json/jugadores.json"
url_tablero = "./json/tablero.json"
url_categorias = "./json/categorias.json"

def principio_juego_pygame(pantalla, fuente, fondo, hay_musica, boton_mute, icon_sonido, icon_mute):
                    
        while True:            
                # Devuelve 2, 3 o 4
                cantidad, hay_musica = seleccionar_cantidad_jugadores(pantalla, fuente, fondo, hay_musica, boton_mute , icon_sonido , icon_mute)
                if cantidad is None:
                    # volver al menú principal sin romper
                    continue
                #sonido_click.play()
                
                jugadores, hay_musica = ingresar_nombres(pantalla, fuente, cantidad, fondo, hay_musica, boton_mute, icon_sonido, icon_mute)
                if jugadores is None:
                    # volver al menú principal sin romper
                    continue
                nombres_jugadores = construir_jugadores(jugadores)
                jugadores_guardados = guardar_jugadores(nombres_jugadores,url_jugadores)
                tablero = creacion_tablero(url_tablero,url_categorias,url_jugadores)
                
                # Paso 3: decidir orden
                jugadores_ordenados = decidir_orden_pygame(pantalla, fuente, jugadores, fondo, hay_musica, boton_mute, icon_sonido, icon_mute)
                # mostrar orden final
                list_jug_ord, hay_musica = mostrar_orden_final(pantalla, fuente, jugadores_ordenados, fondo, hay_musica, boton_mute, icon_sonido, icon_mute)
                return list_jug_ord
