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

