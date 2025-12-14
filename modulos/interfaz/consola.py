import modulos.logica_juego.juego_funciones as juego

def pedir_conservados(dados):
    cant_dados = len(dados)
    texto = f"Ingrese las posiciones a conservar (1-{cant_dados}, separadas por espacios, o vacío para ninguna): "
    return input(texto).strip()

def esperar_enter(mensaje="Presione Enter para continuar"):
    input(mensaje)

def pedir_texto(mensaje: str) -> str:
    return input(mensaje)

def mostrar_texto(texto):
    print(texto)

def mostrar_dados(dados):
    for i in range(1, len(dados) + 1):
        print(f" D.{i}°", end="  ")
    print()
    for _ in dados:
        print("┌───┐", end="  ")
    print()
    for d in dados:
        print(f"│ {d} │", end="  ")
    print()
    for _ in dados:
        print("└───┘", end="  ")
    print()

def pedir_categoria():
    return input("Ingrese una categoria a anotar: ").strip()

def pedir_categoria_valida(puntajes, categorias, jugador):
    import modulos.logica_juego.juego_funciones as juego

    while True:
        eleccion = pedir_categoria()
        ok, resultado = juego.validar_categoria(
            eleccion, puntajes, categorias, jugador
        )

        if ok:
            texto = f"Elegiste la categoría '{resultado['nombre_cat']}'."
            mostrar_texto(texto)
            return resultado
        else:
            mostrar_texto(resultado)

def pedir_conservados_validos(dados):
    while True:
        eleccion = pedir_conservados(dados)
        ok, resultado = juego.validar_conservados(dados, eleccion)
        if ok:
            return resultado
        mostrar_texto(resultado)

def mostrar_decidir_orden(jugadores_ordenados):
    mostrar_texto(
        "<<<<<<------ Tiren los dados para decidir quien comienza ------>>>>>>"
    )

    for jug in jugadores_ordenados:
        mostrar_texto(f"{jug['nombre']} tiró:")
        mostrar_dados([jug["dado"]])
        print()

    ganador = jugadores_ordenados[0]
    mostrar_texto(f"\nEl jugador {ganador['nombre']} comienza primero.\n")

def mostrar_empate():
    mostrar_texto("Hay empate. Se vuelven a tirar los dados.\n")

def pedir_nombres_jugadores(cantidad: int) -> list[str]:
    nombres = []
    for i in range(cantidad):
        nombre = pedir_texto(f"Ingrese el nombre del jugador {i + 1}: ").strip()
        while nombre == "":
            mostrar_texto("Ingrese un nombre correcto.")
            nombre = pedir_texto(f"Ingrese el nombre del jugador {i + 1}: ").strip()
        nombres.append(nombre)
    return nombres

def mostrar_tablero(tablero):
    encabezado = "╔" + "═" * 15 + "╦" + ("═" * 15 + "╗") * len(tablero[1])
    print(encabezado)

    fila_nombres = "║" + f"{'':15}║"
    fila_separador = "╠" + "═" * 15 + "╬"

    for jug in tablero[1]:
        fila_nombres += f"{jug['nombre']:^15}║"
        fila_separador += "═" * 15 + "╬"

    fila_separador = fila_separador[:-1] + "╣"
    print(fila_nombres)
    print(fila_separador)

    categorias = list(tablero[1][0]["puntaje"].keys())
    for categoria in categorias:
        fila = f"║{categoria:^15}║"
        for jug in tablero[1]:
            punt = jug["puntaje"][categoria]
            fila += f"{int(punt):^15}║"
        print(fila)
        separador = "╠" + "═" * 15 + "╬" + ("═" * 15 + "╬") * len(tablero[1])
        print(separador)

    fila_total = "║" + f"{'PUNTAJE TOTAL':^15}║"
    for jug in tablero[1]:
        fila_total += f"{jug['puntajeTotal']:^15}║"
    pie = "╚" + "═" * 15 + "╩" + ("═" * 15 + "╝") * len(tablero[1])

    print(fila_total)
    print(pie)

def mostrar_estadisticas(top10):
    if not top10:
        print("Aún no hay estadísticas guardadas.")
        return
    
    print("\n===== TOP 10 =====")
    for i, est in enumerate(top10, start=1):
        print(f"{i}. {est['nombre']:12} {est['puntaje_total']} puntos")

def mostrar_creditos():
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