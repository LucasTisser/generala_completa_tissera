import json
import os

escritura = "w"
lectura = "r"
append = "a"
# Construye cada jugador
def construir_jugadores(nombres: list[str]) -> list[dict]:
    jugadores = []
    for nombre_jug in nombres:
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
    return jugadores

# Guarda la lista de jugadores en el JSON
def guardar_jugadores(jugadores: list[dict], nombre_archivo: str) -> None:
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(jugadores, archivo, indent=4)

# Se encarga de crear el tablero al principio del juego
# Tambien lo guarda en un archivo json
def creacion_tablero(nombre_archivo_tablero, nombre_archivo_categorias, nombres_archivo_jugadores):
    with open(nombre_archivo_tablero, escritura, encoding="utf-8") as archivo_tablero, \
        open(nombre_archivo_categorias, lectura, encoding="utf-8") as archivo_categorias, \
        open(nombres_archivo_jugadores, lectura, encoding="utf-8") as archivo_jugadores:

        categorias = json.load(archivo_categorias)
        nombres_jugadores = json.load(archivo_jugadores)

        nombres_categorias = [c["Nombre"] for c in categorias]
        puntos_jugs = [jug for jug in nombres_jugadores]

        datos_tablero = [nombres_categorias, puntos_jugs]
        json.dump(datos_tablero, archivo_tablero, indent=4)
    
    return datos_tablero

def puntos_jug_tablero(nombre_archivo_tablero):
    with open(nombre_archivo_tablero,lectura,encoding="utf-8") as arch_tab:
        tablero = json.load(arch_tab)
        puntos_jugadores = tablero[1]
        return puntos_jugadores

def obtener_tablero(nombre_arch_tablero):
    with open(nombre_arch_tablero, lectura, encoding="utf-8") as arch_tablero:
        tablero = json.load(arch_tablero)
    return tablero

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

def obtener_estadisticas(ruta_csv_est):
    if not os.path.exists(ruta_csv_est):
        return []   # devuelve lista vacía si no hay estadísticas
    
    estadisticas = []
    with open(ruta_csv_est, lectura, encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for linea in lineas[1:]:
        nombre, puntaje = linea.strip().split(",")
        estadisticas.append({"nombre": nombre, "puntaje_total": int(puntaje)})

    estadisticas.sort(key=lambda x: x["puntaje_total"], reverse=True)
    return estadisticas[:10]   # devuelve el top 10