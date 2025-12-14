import random
import time
import modulos.logica_juego.juego_funciones as p
import modulos.interfaz.consola as ui


# Valida si es un numero
def validar_numero(texto):
    return texto.isdigit()

# Valida que la cantidad de jugadores sea un numero y no un caracter
# Tambien verifica que el numero sea 1,2,3 o 4 , por los jugadores
def validar_cant_jugadores_es_digito_y_entero() -> int:
    jug = ui.pedir_texto("Numero de jugadores(maximo de 4 jugadores): ").strip()
    while not validar_numero(jug) or not (1 < int(jug) <= 4):
        texto_validar = "Ingrese un numero entero valido entre el 2 y el 4."
        ui.mostrar_texto(texto_validar)
        jug = ui.pedir_texto("Numero de jugadores(de 2 a 4 jugadores): ").strip()
    # Una vez la supera al while, retorna la cantidad de jugadores
    jug = int(jug)
    texto_cant_jug = f"Cantidad de jugadores valida: {jug}"
    ui.mostrar_texto(texto_cant_jug)
    return jug

# Valida que no hay empates en la etapa de quien empieza primero
'''
def resolver_empates(dados_jugadores):

    # Mientras haya dados repetidos, seguir intentando
    while True:
        valores = [j["dado"] for j in dados_jugadores]
        # obtengo todos los valores de dado

        # si no hay repetidos, listo
        if len(valores) == len(set(valores)):
            return dados_jugadores   # no hay empate
        texto = "Hay empate!!. Tiren los dados nuevamente."
        ui.mostrar_texto(texto)
        # si hay repetidos, re-tiro para los que empataron
        for i in range(len(dados_jugadores)):
            for j in range(i + 1, len(dados_jugadores)):
                if dados_jugadores[i]["dado"] == dados_jugadores[j]["dado"]:
                    # empate → ambos vuelven a tirar
                    texto_turno_jugador = f"Tira el jugador {dados_jugadores[i]["nombre"]}"
                    ui.mostrar_texto(texto_turno_jugador)
                    ui.esperar_enter("Presione enter para tirar el dado.")

                    dados_jugadores[i]["dado"] = random.randint(1, 6)
                    time.sleep(1)
                    #p.print_dados()
                    ui.mostrar_dados([dados_jugadores[i]["dado"]])
                    print()

                    texto_turno_jugador2 = f"Tira el jugador {dados_jugadores[j]["nombre"]}"
                    ui.mostrar_texto(texto_turno_jugador2)
                    ui.esperar_enter("Presione enter para tirar el dado.")


                    dados_jugadores[j]["dado"] = random.randint(1, 6)
                    time.sleep(1)
                    #p.print_dados()
                    ui.mostrar_dados([dados_jugadores[j]["dado"]])
                    print()
'''

def resolver_empates(dados_jugadores):
    """
    Recibe una lista de dicts con:
    { "nombre": str, "dado": int }

    Modifica los dados hasta que no haya empates.
    NO imprime, NO pide input.
    """
    # resolver empates
    while True:
            valores = [j["dado"] for j in dados_jugadores]
            if len(valores) == len(set(valores)):
                break

            ui.mostrar_empate()

            for j in dados_jugadores:
                if valores.count(j["dado"]) > 1:
                    ui.esperar_enter(
                        f"Turno de {j['nombre']}. Presione Enter para volver a tirar."
                    )
                    j["dado"] = random.randint(1, 6)
                    ui.mostrar_dados([j["dado"]])
                    print()

