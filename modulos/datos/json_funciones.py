import json
import os

# todos se ponen como default si se pone vacio para que no se tenga que escribir todo manualmente 10 veces
# por eso hay muchas condicionales donde es ''

def cargar_json(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as ar:
            lista_json = json.load(ar) 
            return lista_json
    print(f'Archivo en "{archivo}" no encontrado.')
    default = { # default si no hay nada
        "Nombre": "Uno",
        "Tipo": "suma",
        "Requerimiento": "1",
        "Puntaje": "ninguno"} * 3
    return default


def ingresar_categoria(default:str):
    while True:
        tipo = input('Elige un tipo de categoria. 1 para suma, 2 para puntos estaticos. (E.J. Unos es la suma de todos los unos, Generala siempre es 50.): ').strip()
        if tipo == '1':
            tipo = 'suma'
            break
        elif tipo == '2':
            tipo = 'estatico'
            break
        elif tipo == '':
            tipo = default
            break
        print('Opcion no valida.')

    # default no es una lista aca ya que solamente son 2 opciones y todas despues del 6 son puntos estaticos que siempre son iguales. 
    # mientras tanto otros son sumas de dados de tal valor.
    # se elige con 1 y 2 ya que solamente son 2 opciones y es mas simple que fijarse todos los tipos de formas de escribir suma y estatico.
    return tipo

def ingresar_requerimiento(default, loop:int):
    if default is None: 
        default = ['1'] * (loop+1) # no creo que sea necesario pero hice que se inicialize la lista default si es que esta vacio

    while True:
        requerimiento = input('Ingrese su requerimiento (1-6, todo, secuencia, trio y pareja, cuatro iguales): ').strip()
        entrada = requerimiento.lower() # use otra variable para las condicionales para ser mas corto de leer y para no mezclar funciones de string

        if entrada in ['trio y pareja', 'pareja y trio', '2 y 3', '3 y 2']:
            requerimiento = '2 y 3'
            break
        elif entrada in ['cuatro iguales', '4 y 1', '1 y 4']:
            requerimiento = '4 y 1'
            break
        elif entrada in ['todos iguales', 'todos']:
            requerimiento = 'todos'
            break
        elif entrada in ['sequencia', 'secuencia']:
            requerimiento = 'secuencia'
            break
        elif requerimiento.isdigit() and 0 < int(requerimiento) < 7:
            break
        elif requerimiento == '':
            requerimiento = default[loop]
            break
        print('Opcion no valida')

    # parecido al otro pero con mas condicionales ya que son varias posibilidades. se usa strip para sacar espacios al inicio y el final
    return requerimiento

def ingresar_puntaje(default, loop:int, tipo:str):
    if default is None:
        default = ['1'] * (loop+1) # lo mismo de default que arriba

    while True:
        if tipo == 'suma':
            puntaje = 'ninguno' 
            break # si el tipo es suma se pone como ninguno y termina sin ingresar nada, ya que el puntaje es solo cuando es estatico
        puntaje = input('Ingrese un puntaje por default (E.j Generala = 50 puntos): ').strip()
        if puntaje.isdigit():
            break # se fija si es un digito y termina
        elif puntaje == '':
            puntaje = default[loop]
            break
        print('Opcion no valida.')

    return puntaje

def iniciar_json():
    os.makedirs("json", exist_ok=True) # hacer el directorio si no existe ya
    json_actual = 'json/categorias.json' # json actual es la destinacion. cambia a categorias_2, 3... si no se sobreescribe.
    if os.path.exists('json/categorias.json'):
        while True:
            # si existe, se puede elegir si sobreescribirlo, hacer uno nuevo o cancelar
            continuar = input('Este archivo Json ya existe. Desea sobreescribirlo? Ingrese una opcion: \n1) Sobreescribir archivo \n2) Crear archivo nuevo \n3) Cancelar\n')
            if continuar == '1':
                break
            elif continuar == '2':
                # si se hace uno nuevo, se cuenta cuantos categorias_x.json hay y se hace uno mas, asi no se sobreescriben
                contador = 2
                while os.path.exists(f"json/categorias_{contador}.json"):
                    contador += 1
                json_actual = f"json/categorias_{contador}.json"
                break

            elif continuar == '3':
                print('Operacion cancelada.')
                return
            else:
                print('Opcion no valida.')

    # listas para valores default
    nombres_default = ['Unos', 'Doses', 'Treses', 'Cuatros', 'Cincos', 'Seises', 'Escalera', 'Full', 'Poker', 'Generala']
    # tipo = primeros 6 suma, demas estatico 
    tipo_default = ''
    requerimiento_default = ['1', '2', '3', '4', '5', '6', 'secuencia', '2 y 3', '4 y 1', 'todos']
    puntajes_default = ['ninguno', 'ninguno', 'ninguno', 'ninguno', 'ninguno', 'ninguno', '20', '30', '40', '50']

    nuevo_json = []

    # 10 porque el pdf del parcial mencionaba a 10 en lugar de 13.
    # primero se hace varios print asi se muestran cual es el default
    for i in range(10):
        print(f'\nIngresando categoria {i+1}. Por default: \nNombre: {nombres_default[i]}')
        requerimiento_texto = requerimiento_default[i]
        if i < 6:
            tipo_default = 'suma'

            print('Tipo: Suma')
            print(f'Numero requerido: {requerimiento_default[i]}')

        else:
            tipo_default = 'estatico'
            if i == 7:
                requerimiento_texto = "trio y pareja"
            elif i == 8:
                requerimiento_texto = "cuatro iguales"

            print('Tipo: Estatico')
            print(f'Combinacion requerida: {requerimiento_texto}')
            print(f'Puntos: {puntajes_default[i]}')
        
        print('')
        # ^ print para que haya una linea entre los defaults y los valores a ingresar
        # despues todas las funciones y el nombre, que es solamente 3 lineas y no necesita una funcion.

        nombre = input('Ingrese el nombre de su categoria: ').strip()
        if nombre == '':
            nombre = nombres_default[i]

        tipo = ingresar_categoria(tipo_default)
        
        requerimiento = ingresar_requerimiento(requerimiento_default, i)

        puntaje = ingresar_puntaje(puntajes_default, i, tipo)
        
        # se envia a la lista como llaves de diccionario
        nuevo_json.append({"Nombre":  nombre,
                            "Tipo": tipo,
                            "Requerimiento": requerimiento,
                            "Puntaje": puntaje})
        
    # y se añade
    with open(json_actual, 'w', encoding='utf-8') as archivo:
        json.dump(nuevo_json, archivo, indent=4)
    return
