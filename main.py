# Importante antes de iniciar la virtual enviorment (venv)
# 1 usar este comando en la terminal: 
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# luego se puede usar la inicializacion de la venv "generala_env"
# .\generala_env\Scripts\Activate.ps1
# Solo pasa en mi computadora, desconozco de las demas
# Luego de estar sobre la venv, instalamos pygame con el siguiente comando
# pip install pygame

# Para abrir pygame, ejecutar el siguiente comando en esta raiz
# python -m modulos.interfaz.pygame_interface.ui_pygame


import modulos.juego_estado as juego
import modulos.datos.datos_funciones as d
import modulos.interfaz.consola as ui

nombre_archivo_estadistica = "./json/estadisticas.csv"

while True:
    print("""
================
    GENERALA
================
Opciones: 
1) Jugar
2) Estadisticas
3) Creditos
4) Salir
    """) 

    try:
        opcion = int(input('Su opcion: '))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue

    if opcion == 1: 
        juego.comenzar_juego()
    elif opcion == 2:
        top10 = d.obtener_estadisticas(nombre_archivo_estadistica)
        ui.mostrar_estadisticas(top10)
    elif opcion == 3:
        ui.mostrar_creditos()
    elif opcion == 4:
        print('Gracias por jugar')
        break
    else:
        print('Opcion no valida')
