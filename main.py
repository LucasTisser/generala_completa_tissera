import modulos.juego_estado as juego
import modulos.datos.datos_funciones as r

nombre_archivo_estadistica = "./json/estadisticas.csv"

while True:
    mensaje_info =print("""
================
    GENERALA
================
Opciones: 
1)Jugar. 
2)Estadisticas. 
3)Creditos. 
4) Salir
                        """) 
    opcion = int(input('Su opcion: '))
    if opcion == 1: 
        juego.comenzar_juego()
    elif opcion == 2:
        r.mostrar_estadisticas(nombre_archivo_estadistica)
    elif opcion == 3:
        r.print_creditos()
    elif opcion == 4:
        print('Gracias por jugar')
        break
    else:
        print('Opcion no valida')