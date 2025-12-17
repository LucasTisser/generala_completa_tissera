from modulos.interfaz.pygame_interface.core.init import init_pygame, pantalla_pygame,fuente_pygame,clock_pygame,musica_activa_pygame
from modulos.interfaz.pygame_interface.core.assets import cargar_musica_fondo, cargar_musica_fondo_aves
from modulos.interfaz.pygame_interface.screens.menu_principal import menu_principal_pygame

dados = [1, 2, 3, 4, 5]
conservados = [False, False, False, False, False]
tiros_restantes = 3
#botones_jugadas = crear_botones_jugadas(fuente, 50, 100, dados)

def main():
    init_pygame()
    pantalla = pantalla_pygame()
    fuente = fuente_pygame()
    clock = clock_pygame()
    musica_activa = musica_activa_pygame()
    cargar_musica_fondo()
    cargar_musica_fondo_aves()
    
    menu_principal_pygame(pantalla, fuente, musica_activa)

if __name__ == "__main__":
    main()