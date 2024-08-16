import pygame
import sys
from config import WIDTH, HEIGHT

def iniciar_ventana():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego en Python")
    return window