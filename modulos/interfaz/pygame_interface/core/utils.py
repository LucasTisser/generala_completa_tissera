import pygame

def toggle_musica(musica_act):
    if musica_act:
        pygame.mixer.music.pause()
        return False
    else:
        pygame.mixer.music.unpause()
        return True

def manejar_hover(lista_botones, pos, sonido_hover=None):
    """
    Actualiza el estado hover de una lista de botones.
    - lista_botones: lista de diccionarios de botones
    - pos: posición actual del mouse
    - sonido_hover: opcional, sonido a reproducir al entrar
    """
    for boton in lista_botones:
        if boton["rect"].collidepoint(pos):
            if not boton["hover"]:
                boton["hover"] = True
                if sonido_hover:
                    sonido_hover.play()
        else:
            boton["hover"] = False