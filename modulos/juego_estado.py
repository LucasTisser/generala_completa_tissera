import modulos.logica_juego.juego_funciones as j
import modulos.datos.datos_funciones as d
import modulos.interfaz.consola as ui

nombre_archivo_estadistica = "./json/estadisticas.csv"
url_jugadores = "./json/jugadores.json"
url_tablero = "./json/tablero.json"
url_categorias = "./json/categorias.json"

def comenzar_juego():
        rondas = 1
        ganador_y_est = dict()
        categorias = j.cargar_categorias()
        lista_jug_ordenada = j.principio_juego(
                pedir_nombres=ui.pedir_nombres_jugadores,
                mostrar_texto=ui.mostrar_texto,
                esperar_turno=ui.esperar_enter,
                mostrar_dados=ui.mostrar_dados
                )

        for i in range(2):
                rondas += 1

                ganador_y_est = j.turno_jugadores(
                rondas,
                lista_jug_ordenada,
                categorias,
                mostrar_texto=ui.mostrar_texto,
                esperar_turno=ui.esperar_enter,
                mostrar_dados=ui.mostrar_dados,
                pedir_conservados=ui.pedir_conservados_validos,
                pedir_categoria=ui.pedir_categoria_valida,
                mostrar_tablero=lambda: ui.mostrar_tablero(d.obtener_tablero(url_tablero)),
                obtener_puntos_jugadores=lambda: d.puntos_jug_tablero(url_tablero),
                actualizar_tablero=lambda jug_puntos: d.actualizar_tablero(url_tablero, jug_puntos, url_jugadores)
                )

        ui.mostrar_texto("< < < < - - - - - - - - - - - - - - - - > > > >")
        ui.mostrar_texto("\t \t JUEGO FINALIZADO")
        ui.mostrar_texto("< < < < - - - - - - - - - - - - - - - - > > > >")
        ui.mostrar_texto(
                f" Gano {ganador_y_est['ganador']['nombre']}, "
                f"con un total de {ganador_y_est['ganador']['puntajeTotal']} puntos.\n"
                f"\t     Felicitaciones ! ! ! "
        )
        ui.mostrar_texto("< < < < - - - - - - - - - - - - - - - - > > > >")

        est_cont = ganador_y_est["estadistica"]
        d.guardar_estadistica(est_cont, nombre_archivo_estadistica)