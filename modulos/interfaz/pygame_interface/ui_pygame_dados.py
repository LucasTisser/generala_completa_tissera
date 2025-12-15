import pygame

imagenes_dados = {
    1: pygame.image.load("assets/imagenes/1_dot.png"),
    2: pygame.image.load("assets/imagenes/2_dot.png"),
    3: pygame.image.load("assets/imagenes/3_dot.png"),
    4: pygame.image.load("assets/imagenes/4_dot.png"),
    5: pygame.image.load("assets/imagenes/5_dot.png"),
    6: pygame.image.load("assets/imagenes/6_dot.png"),
}

'''
def mostrar_dados(pantalla, dados, x, y, tamaño=100):
    for i, valor in enumerate(dados):
        imagen = pygame.transform.scale(imagenes_dados[valor], (tamaño, tamaño))
        pantalla.blit(imagen, (x + i*(tamaño+20), y))
'''

def mostrar_dados(pantalla, dados, conservados, x, y, tamaño=100):
    rects = []
    for i, valor in enumerate(dados):
        imagen = pygame.transform.scale(imagenes_dados[valor], (tamaño, tamaño))
        rect = pygame.Rect(x + i*(tamaño+20), y, tamaño, tamaño)
        pantalla.blit(imagen, rect.topleft)

        # Si el dado está conservado → dibujar borde rojo
        if conservados[i]:
            pygame.draw.rect(pantalla, (200,0,0), rect, 4)
        else:
            pygame.draw.rect(pantalla, (0,0,0), rect, 2)

        rects.append(rect)
    return rects