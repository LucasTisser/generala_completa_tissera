import pygame
from modulos.interfaz.pygame_interface.ui_pygame_botones import crear_boton, dibujar_boton, clickeado
from modulos.config import OPCIONES_JUGADAS
from modulos.logica_juego.juego_funciones import puntajes_disponibles

def crear_botones_jugadas(fuente, x, y, dados, categorias=OPCIONES_JUGADAS, ancho=250, alto=40, espacio=10):
    botones = []
    puntajes = puntajes_disponibles(dados, categorias)
    
    for i, categoria in enumerate(OPCIONES_JUGADAS):
        texto = f"{categoria['Nombre']} ({puntajes[i]})"
        boton = crear_boton(x, y + i*(alto+espacio), ancho, alto, texto, fuente, (255,255,255))
        botones.append(boton)
    return botones

def mostrar_menu_jugadas(pantalla, botones):
    for boton in botones:
        dibujar_boton(pantalla, boton)

def detectar_jugada_click(pos_mouse, botones):
    for i, boton in enumerate(botones):
        if clickeado(boton, pos_mouse):
            return OPCIONES_JUGADAS[i]
    return None
