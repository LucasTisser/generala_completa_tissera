import random
import json
import os
import time
import modulos.validaciones.valids as v
import modulos.datos.datos_funciones as r

url_jugadores = "./json/jugadores.json"
url_tablero = "./json/tablero.json"
url_categorias = "./json/categorias.json"

def cargar_categorias():
    if not os.path.exists('json/categorias.json'):
        return [] 
    with open('json/categorias.json', 'r', encoding="utf-8")  as info:
        categorias_lista = json.load(info)
        return categorias_lista

def decidir_orden(list_jug, mostrar_texto, esperar_turno, mostrar_dados):
    info_jugadores = []

    mostrar_texto("<<<<<<------ Tiren los dados para decidir quien comienza ------>>>>>>")

    # primer tiro
    for jug in list_jug:
        esperar_turno(f"Turno de {jug['nombre']}. Presione para tirar el dado.")
        dado = random.randint(1, 6)
        info_jugadores.append({
            "nombre": jug["nombre"],
            "dado": dado
        })
        mostrar_dados([dado])

    # resolver empates solo entre los máximos
    while True:
        max_valor = max(j["dado"] for j in info_jugadores)
        maximos = [j for j in info_jugadores if j["dado"] == max_valor]

        if len(maximos) == 1:
            break  # ya hay un único ganador

        mostrar_texto("Hay empate entre los que sacaron el mayor valor. Se vuelven a tirar esos jugadores.")

        # solo los jugadores empatados tiran de nuevo
        for j in maximos:
            esperar_turno(f"Turno de {j['nombre']} para desempatar")
            j["dado"] = random.randint(1, 6)
            mostrar_dados([j["dado"]])

    # ordenar por dado
    info_jugadores.sort(key=lambda j: j["dado"], reverse=True)
    ganador = info_jugadores[0]
    mostrar_texto(f"\nEl jugador {ganador['nombre']} comienza primero.\n")

    return info_jugadores



'''
def principio_juego():
    # 1) pedir cantidad de jugadores (validación)
    cant_jugadores = v.validar_cant_jugadores_es_digito_y_entero()

    # 2) pedir nombres desde la interfaz (consola)
    nombres = ui.pedir_nombres_jugadores(cant_jugadores)

    # 3) construir y guardar jugadores (datos)
    jugadores = r.construir_jugadores(nombres)
    r.guardar_jugadores(jugadores, url_jugadores)

    # 4) crear tablero
    r.creacion_tablero(url_tablero, url_categorias, url_jugadores)

    # 5) decidir orden
    lista_jug_ordenadas = decidir_orden(
        jugadores,
        mostrar_texto=ui.mostrar_texto,
        esperar_turno=ui.esperar_enter,
        mostrar_dados=ui.mostrar_dados
    )
    return lista_jug_ordenadas
'''

def principio_juego(pedir_nombres, mostrar_texto, esperar_turno, mostrar_dados):
    cant_jugadores = v.validar_cant_jugadores_es_digito_y_entero()
    nombres = pedir_nombres(cant_jugadores)
    jugadores = r.construir_jugadores(nombres)
    r.guardar_jugadores(jugadores, url_jugadores)
    r.creacion_tablero(url_tablero, url_categorias, url_jugadores)
    lista_jug_ordenadas = decidir_orden(
        jugadores,
        mostrar_texto=mostrar_texto,
        esperar_turno=esperar_turno,
        mostrar_dados=mostrar_dados
    )
    return lista_jug_ordenadas




def validar_conservados(dados, eleccion: str):
    """
    dados: lista de valores de dados (len = 5)
    eleccion: string ingresado por el usuario

    Retorna:
    (True, lista_indices) si es válido
    (False, mensaje_error) si no es válido
    """
    cant_dados = len(dados)

    # Caso vacío → no conserva ninguno
    if eleccion == "":
        return True, []

    partes = eleccion.split()

    if not all(p.isdigit() for p in partes):
        return False, "Solo se permiten números separados por espacios."

    indices = [int(p) for p in partes]

    if not all(1 <= x <= cant_dados for x in indices):
        return False, f"Las posiciones válidas son del 1 al {cant_dados}."

    # convertir a base 0 y eliminar duplicados
    indices = sorted(set(x - 1 for x in indices))
    return True, indices

def aplicar_conservados_y_tirar(dados_actuales, indices_conservados):
    #   dados_actuales: lista de 5 valores
    #   indices_conservados: lista de índices (base 0) que se conservan
    #   Devuelve la lista resultante (misma longitud), donde los no conservados
    #   han sido re-tirados.
    n = len(dados_actuales)
    #   cuántos hay que tirar
    faltan = [i for i in range(n) if i not in indices_conservados]
    nuevos = tirar_dados(len(faltan))

    resultado = dados_actuales.copy()
    for idx_pos, pos in enumerate(faltan):
        resultado[pos] = nuevos[idx_pos]
    return resultado

def tirar_dados(n):
        return [random.randint(1, 6) for _ in range(n)]

def puntajes_disponibles(dados, categorias):
    resultados = ["0"] * len(categorias)

    for i in range(len(categorias)):
        categoria = categorias[i]
        if categoria["Tipo"] == 'suma':
            # las sumas. se itera por todos los dados y si el requerimiento es un digito (para no crashear) y el dado es igual al requerimiento, se suma al resultado
            resultado_suma = 0
            for j in dados:
                if categoria["Requerimiento"].isdigit() and j == int(categoria["Requerimiento"]):
                    resultado_suma += j
            resultados[i] = resultado_suma
        
        elif categoria["Tipo"] == 'estatico' and categoria["Puntaje"].isdigit():
            # Secuencia. se ordenan los dados de menor a mayor (salteando el primero)
            # si uno NO es 1 mayor que el anterior, se pone es_secuencia = false y queda como 0
            if categoria["Requerimiento"] == 'secuencia':
                valores_ordenados = sorted(dados)
                es_secuencia = True
                for j in range(1, len(valores_ordenados)):
                    if valores_ordenados[j] != valores_ordenados[j-1] + 1:
                        es_secuencia = False
                        break
                if es_secuencia:
                    resultados[i] = int(categoria["Puntaje"])
                else:
                    resultados[i] = 0

            elif categoria["Requerimiento"] == '2 y 3' or categoria["Requerimiento"] == '4 y 1':
                # se ordena y se hace un diccionario 'conteos' donde se añade cada numero nuevo. si no esta en conteos se lo añade, y si ya esta se le suma 1 a la cantidad 
                conteos = {}
                for j in dados:
                    if j in conteos:
                        conteos[j] += 1
                    else:
                        conteos[j] = 1
                # se itera por cada valor en conteos para ver si tiene la cantidad
                hay_3 = False
                hay_2 = False
                hay_4 = False
                for j in conteos.values():
                    if j == 3:
                        hay_3 = True
                    elif j == 2:
                        hay_2 =  True
                    elif j == 4:
                        hay_4 = True
                
                # condicionales para añadir el puntaje o no
                if categoria["Requerimiento"] == '2 y 3':
                    if hay_3 and hay_2:
                        resultados[i] = int(categoria["Puntaje"])
                    else:
                        resultados[i] = 0
                elif categoria["Requerimiento"] == '4 y 1':
                    if hay_4:
                        resultados[i] = int(categoria["Puntaje"])
                    else:
                        resultados[i] = 0

            # si se encuentra uno diferente se pone como falso
            elif categoria["Requerimiento"] == 'todos':
                todos_iguales = True
                for j in range(1, len(dados)):
                    if dados[j] != dados[j-1]:
                        todos_iguales = False
                        break
                if todos_iguales:
                    resultados[i] = int(categoria["Puntaje"])
                else:
                    resultados[i] = 0

            #agregar que cuando sea el primer tiro sume 100 puntos
    return resultados

def validar_categoria(eleccion: str, puntajes, categorias, jugador):
    """
    Retorna:
    (True, dict) si es válida
    (False, mensaje_error) si no lo es
    """
    if not eleccion.isdigit():
        return False, "Debe ingresar un número."

    idx = int(eleccion) - 1
    if not (0 <= idx < len(categorias)):
        return False, "Número fuera de rango."

    nombre_cat = categorias[idx]["Nombre"]

    # ya anotada
    if jugador["puntaje"][nombre_cat] != "0":
        return False, f"Ya anotaste en '{nombre_cat}'. Elegí otra categoría."

    return True, {
        "nombre_cat": nombre_cat,
        "puntaje": puntajes[idx]
    }

# Funcion central para determinar el ganador de la partida
# Se encarga de los turnos de todos los jugadores a traves de un ciclo
def turno_jugadores(
    rondas,
    list_jug,
    categorias,
    mostrar_texto,
    esperar_turno,
    mostrar_dados,
    pedir_conservados,
    pedir_categoria,
    mostrar_tablero,
    obtener_puntos_jugadores,
    actualizar_tablero
):
    mostrar_texto(f"\t\tRonda {rondas - 1}")

    for jugador in list_jug:
        # Turno del jugador
        mostrar_texto("< < < < - - - - - - - - - - - - - - - - > > > >")
        mostrar_texto(f"\t\tTurno de {jugador['nombre']}")
        mostrar_texto("< < < < - - - - - - - - - - - - - - - - > > > >")

        # ===== PRIMER TIRO =====
        esperar_turno("Presione enter para el tiro 1")
        time.sleep(2)
        dados = tirar_dados(5)
        mostrar_tablero()
        mostrar_texto("Primer Tiro:")
        mostrar_dados(dados)
        conservados = pedir_conservados(dados)

        # ===== SEGUNDO TIRO =====
        esperar_turno("Presione enter para el tiro 2")
        time.sleep(2)
        dados = aplicar_conservados_y_tirar(dados, conservados)
        mostrar_tablero()
        mostrar_texto("Segundo Tiro:")
        mostrar_dados(dados)
        conservados = pedir_conservados(dados)

        # ===== TERCER TIRO =====
        esperar_turno("Presione enter para el tiro 3")
        time.sleep(2)
        dados = aplicar_conservados_y_tirar(dados, conservados)
        mostrar_tablero()
        mostrar_texto("Tercer tiro:")
        mostrar_dados(dados)

        # ===== PUNTAJES =====
        puntos_jugs = obtener_puntos_jugadores()
        tabla_puntajes = puntajes_disponibles(dados, categorias)

        mostrar_texto('--------- Posibles opciones de anotar --------')
        for i in range(len(categorias)):
            mostrar_texto(f'{i+1}). {categorias[i]["Nombre"]}: {tabla_puntajes[i]}')

        # Buscar jugador actual en puntos_jugs
        jug = next((pj for pj in puntos_jugs if pj["nombre"] == jugador["nombre"]), {})

        cat_y_puntos = pedir_categoria(tabla_puntajes, categorias, jug)

        jug_puntos = {
            "nombre": jugador["nombre"],
            "categoria": cat_y_puntos["nombre_cat"],
            "valor": cat_y_puntos["puntaje"]
        }

        actualizar_tablero(jug_puntos)
        mostrar_tablero()

    # ===== DETERMINAR GANADOR =====
    puntos_jugs = obtener_puntos_jugadores()
    punt_ganador = 0
    ganador = {}
    est_cont = []

    for pj in puntos_jugs:
        if pj["puntajeTotal"] > punt_ganador:
            punt_ganador = pj["puntajeTotal"]
            ganador = pj
        est_cont.append({"nombre": pj["nombre"], "puntaje_total": pj["puntajeTotal"]})

    return {"ganador": ganador, "estadistica": est_cont}