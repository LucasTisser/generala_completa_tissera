import pygame

def mostrar_dados(pantalla, dados, x, y, tamaño=60):
    fuente = pygame.font.Font(None, 40)
    for i, valor in enumerate(dados):
        rect = pygame.Rect(x + i*(tamaño+10), y, tamaño, tamaño)
        pygame.draw.rect(pantalla, (200,200,200), rect)  # cuadrado gris
        texto = fuente.render(str(valor), True, (0,0,0))
        pantalla.blit(texto, (rect.x + tamaño//3, rect.y + tamaño//3))
