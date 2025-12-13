import random
import time
import modulos.logica_juego.juego_funciones as p

# Valida si es un numero
def validar_numero(texto):
    return texto.isdigit()

# Valida que la cantidad de jugadores sea un numero y no un caracter
# Tambien verifica que el numero sea 1,2,3 o 4 , por los jugadores
def validar_cant_jugadores_es_digito_y_entero() -> int:
    jug = input("Numero de jugadores(maximo de 4 jugadores): ").strip()
    while not validar_numero(jug) or not (1 < int(jug) <= 4):
        print("Ingrese un numero entero valido entre el 2 y el 4.")
        jug = input("Numero de jugadores(de 2 a 4 jugadores): ").strip()

    # Una vez la supera al while, retorna la cantidad de jugadores
    jug = int(jug)
    print(f"Cantidad de jugadores valida: {jug}")
    return jug

# Valida que no hay empates en la etapa de quien empieza primero
def resolver_empates(dados_jugadores):
    # Mientras haya dados repetidos, seguir intentando
    while True:
        valores = [j["dado"] for j in dados_jugadores]
        # obtengo todos los valores de dado

        # si no hay repetidos, listo
        if len(valores) == len(set(valores)):
            return dados_jugadores   # no hay empate

        print("Hay empate!!. Tiren los dados nuevamente.")
        # si hay repetidos, re-tiro para los que empataron
        for i in range(len(dados_jugadores)):
            for j in range(i + 1, len(dados_jugadores)):
                if dados_jugadores[i]["dado"] == dados_jugadores[j]["dado"]:
                    # empate → ambos vuelven a tirar
                    
                    print(f"Tira el jugador {dados_jugadores[i]["nombre"]}")
                    input("Presione enter para tirar el dado.")
                    dados_jugadores[i]["dado"] = random.randint(1, 6)
                    time.sleep(1)
                    p.print_dados([dados_jugadores[i]["dado"]])
                    print()

                    print(f"Tira el jugador {dados_jugadores[j]["nombre"]}")
                    input("Presione enter para tirar el dado.")
                    dados_jugadores[j]["dado"] = random.randint(1, 6)
                    time.sleep(1)
                    p.print_dados([dados_jugadores[j]["dado"]])
                    print()