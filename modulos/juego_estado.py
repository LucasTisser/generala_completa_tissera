#import modulos.json_funciones as jason
import modulos.logica_juego.juego_funciones as j
import modulos.datos.datos_funciones as d

nombre_archivo_estadistica = "./json/estadisticas.csv"

def comenzar_juego():
        rondas = 1
        ganador_y_est = dict()
        categorias = j.cargar_categorias()
        lista_jug_ordenada = j.principio_juego()
        for i in range(len(categorias)):
                rondas += 1
                ganador_y_est = j.turno_jugadores(rondas, lista_jug_ordenada, categorias)
        print("< < < < - - - - - - - - - - - - - - - - > > > >")
        print(f"\t \t JUEGO FINALIZADO")
        print("< < < < - - - - - - - - - - - - - - - - > > > >")
        print(f"\t    Gano {ganador_y_est["ganador"]["nombre"]}, con un total de {ganador_y_est["ganador"]["puntajeTotal"]} puntos.\n \t     Felicitaciones ! ! ! ")
        print("< < < < - - - - - - - - - - - - - - - - > > > >")
        
        est_cont = ganador_y_est["estadistica"]
        d.guardar_estadistica(est_cont, nombre_archivo_estadistica)