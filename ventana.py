import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego en Python")

# Definir el color del personaje (circulo) y la sala
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
player_color = (0, 0, 255)
player_radius = 20

# Posición inicial del jugador
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Lógica del juego
    window.fill(BLACK)  # Pintar la pantalla de negro
    pygame.draw.circle(window, player_color, (player_x, player_y), player_radius)  # Dibujar el jugador
    pygame.display.update()  # Actualizar la pantalla

