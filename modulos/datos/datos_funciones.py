import json
import os

escritura = "w"
lectura = "r"
append = "a"
# Por partida, registra cada jugador, y guarda los datos para la partida, en un archivo json
# Si se crea otra partida nueva, los nuevos jugadores pisan a los viejos, dejando solos los nuevos
def registrar_jugador(cant_jug,nombre_archivo):
    jugadores = []
    escritura = "w"
    
    with open(nombre_archivo, escritura , encoding="utf-8") as archivo:
        for i in range(cant_jug):
            nombre_jug = input(f"Ingrese en nombre del jugador {i + 1} :").strip()

            while nombre_jug == "":
                print("Ingrese un nombre correcto")
                nombre_jug = input(f"Ingrese en nombre del jugador {i + 1} :").strip()
            
            datos_jug = {
                "nombre": nombre_jug,
                "puntaje":  {
                        "Unos" : "0",
                        "Doses" : "0",
                        "Treses": "0",
                        "Cuatros": "0",
                        "Cincos": "0",
                        "Seises": "0",
                        "Escalera": "0",
                        "Full": "0",
                        "Poker": "0",
                        "Generala": "0",
                },
                "puntajeTotal": 0,
            }
            jugadores.append(datos_jug)
        json.dump(jugadores, archivo, indent=4)
    return jugadores

#Se encarga de crear el tablero al principio del juego, justo despues de pedir nombres y antes de que tiren los dados
#Tambien lo guarda en un archivo json para que luego en otra funcion vaya actualizando los puntos 
def creacion_tablero(nombre_archivo_tablero, nombre_archivo_categorias, nombres_archivo_jugadores):

    with open(nombre_archivo_tablero,escritura,encoding="utf-8") as archivo_tablero, \
            open(nombre_archivo_categorias, lectura, encoding="utf-8") as archivo_categorias, \
                open(nombres_archivo_jugadores,lectura,encoding="utf-8") as archivo_jugadores:
                    categorias = json.load(archivo_categorias)
                    nombres_jugadores = json.load(archivo_jugadores)

                    encabezado = "╔" + "═" * 15 + "╦" + ("═" * 15 + "╗") * len(nombres_jugadores)
                    print(encabezado)
                    fila_nombres = "║"
                    fila_separador = "╠"

                    # primer bloque vacío
                    fila_nombres += f"{'':15}║"
                    fila_separador += "═" * 15 + "╬"

                    # columnas para cada jugador
                    for jug in nombres_jugadores:
                            fila_nombres += f"{jug['nombre']:^15}║"
                            fila_separador += "═" * 15 + "╬"

                    # reemplazar último "╬" por "╣"
                    fila_separador = fila_separador[:-1] + "╣"

                    print(fila_nombres)
                    print(fila_separador)
                    
                    # ---- CATEGORÍAS ----
                    for categoria in categorias:
                        nombre_categoria = f"║{categoria['Nombre']:^15}║" + (" " * 7 + f"{int(0)}" + " " * 7+ "║") * len(nombres_jugadores)
                        separador = "╠" + "═" * 15 + "╬" + ("═" * 15 + "╬") * len(nombres_jugadores)
                        print(nombre_categoria)
                        print(separador)
                    
                    # TOTALES
                    fila_total = "║" + f"{'PUNTAJE TOTAL':^15}║"

                    # Cuando tengan puntajes reales, quitar el 0 del ciclo y descomentar lo siguiente
                    for jug in nombres_jugadores:
                        fila_total += f"{jug["puntajeTotal"]:^15}║"

                    pie ="╚" + "═" * 15 + "╩" + ("═" * 15 + "╝") * len(nombres_jugadores)

                    print(fila_total)
                    print(pie)

                    #   Guarda los datos importantes en un json "tablero.json"
                    #   Luego en otra funcion se actualizaran los puntos durante el juego
                    nombres_categorias = []
                    for categoria in categorias:
                        nombres_categorias.append(categoria["Nombre"])

                    puntos_jugs = []
                    for jug in nombres_jugadores:
                        puntos_jugador = jug
                        puntos_jugs.append(puntos_jugador)

                    datos_tablero = [nombres_categorias,puntos_jugs]   
                    json.dump(datos_tablero,archivo_tablero,indent=4)

def puntos_jug_tablero(nombre_archivo_tablero):
    with open(nombre_archivo_tablero,lectura,encoding="utf-8") as arch_tab:
        tablero = json.load(arch_tab)
        puntos_jugadores = tablero[1]
        return puntos_jugadores

def print_tablero(nombre_arch_tablero):
    with open(nombre_arch_tablero,lectura,encoding="utf-8") as arch_tablero:
        tablero = json.load(arch_tablero)
        encabezado = "╔" + "═" * 15 + "╦" + ("═" * 15 + "╗") * len(tablero[1])
        print(encabezado)
        fila_nombres = "║"
        fila_separador = "╠"

        # primer bloque vacío
        fila_nombres += f"{'':15}║"
        fila_separador += "═" * 15 + "╬"

        # columnas para cada jugador
        for jug in tablero[1]:
                fila_nombres += f"{jug['nombre']:^15}║"
                fila_separador += "═" * 15 + "╬"

        # reemplazar último "╬" por "╣"
        fila_separador = fila_separador[:-1] + "╣"

        print(fila_nombres)
        print(fila_separador)

        categorias = list(tablero[1][0]["puntaje"].keys())

        # ---- CATEGORÍAS ----
        for categoria in categorias:
            fila = f"║{categoria:^15}║"
            for jug in tablero[1]:
                punt = jug["puntaje"][categoria]
                fila += f"{int(punt):^15}║"
            print(fila)

            # separador de categorías
            separador = "╠" + "═" * 15 + "╬" + ("═" * 15 + "╬") * len(tablero[1])
            print(separador)
        # TOTALES
        fila_total = "║" + f"{'PUNTAJE TOTAL':^15}║"

        # Cuando tengan puntajes reales, quitar el 0 del ciclo y descomentar lo siguiente
        for jug in tablero[1]:
            fila_total += f"{jug["puntajeTotal"]:^15}║"

        pie ="╚" + "═" * 15 + "╩" + ("═" * 15 + "╝") * len(tablero[1])
        print(fila_total)
        print(pie)

def actualizar_tablero(nombre_arch_tablero,datos_nuevos, nombre_arch_jugadores):
    with open(nombre_arch_tablero,lectura,encoding="utf-8") as arch_tabl, \
        open(nombre_arch_jugadores,lectura,encoding="utf-8") as archivo_jugadores:
            tablero = json.load(arch_tabl)
            arch_jug = json.load(archivo_jugadores)
            nombre_buscado = datos_nuevos["nombre"]
            categoria = datos_nuevos["categoria"]
            valor = datos_nuevos["valor"]

            jugadores_tablero = tablero[1]

            for jug in jugadores_tablero:
                if jug["nombre"] == nombre_buscado:

                    # Actualiza el puntaje en el tablero
                    jug["puntaje"][categoria] = valor

                    # Actualiza puntaje total
                    jug["puntajeTotal"] = sum(
                        int(v) for v in jug["puntaje"].values() if v is not None
                    )

                    #Actualizo arch_jug
                    for jug_arch in arch_jug:
                        if jug_arch["nombre"] == jug["nombre"]:
                            jug_arch["puntaje"] = {
                                cat: v for cat, v in jug["puntaje"].items()
                            }
                            jug_arch["puntajeTotal"] = jug["puntajeTotal"]
                            break
                    break

        # Guardar cambios
    with open(nombre_arch_tablero, escritura, encoding="utf-8") as arch:
        json.dump(tablero, arch, indent=4)
    
    with open(nombre_arch_jugadores,escritura,encoding="utf-8") as ar_ju:
        json.dump(arch_jug,ar_ju, indent=4)

def guardar_estadistica(jugadores, ruta_csv_est):
    # Revisar si existe el archivo
    archivo_existe = os.path.exists(ruta_csv_est)

    with open(ruta_csv_est, append, encoding="utf-8") as archivo:
        # Si el archivo no existe, escribir encabezado
        if not archivo_existe:
            archivo.write("nombre,puntaje\n")

        # Guardar cada jugador
        for jug in jugadores:
            linea = f"{jug['nombre']},{jug['puntaje_total']}\n"
            archivo.write(linea)


def mostrar_estadisticas(ruta_csv_est):
    if not os.path.exists(ruta_csv_est):
        print("Aún no hay estadísticas guardadas.")
        return
    
    estadisticas = []

    with open(ruta_csv_est,lectura, encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for linea in lineas[1:]:
        nombre, puntaje = linea.strip().split(",")
        estadisticas.append({"nombre": nombre, "puntaje_total": int(puntaje)})

    estadisticas.sort(key=lambda x: x["puntaje_total"], reverse=True)

    top10 = estadisticas[:10]

    print("\n===== TOP 10 =====")
    for i, est in enumerate(top10, start=1):
        print(f"{i}. {est['nombre']:12} {est['puntaje_total']} puntos")

def print_creditos():
    print("------------------------------------------------------")
    print("\t\tMINI GENERALA TEMATICA")
    print("------------------------------------------------------")
    print("Author/es: Tissera Lucas y Acevedo Ivan")
    print("Fecha: NOV-DIC 2025")
    print("Materia: Programacion I")
    print("Docentes: Martín Alejandro García")
    print("Carrera: Tecnicatura en Programacion Informatica")
    print("Contacto: lucas.tissera@hotmail.com")
    print("------------------------------------------------------")