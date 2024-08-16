import random
import sys
import pygame
import 

# Definir enemigo
enemy_color = (255, 0, 0)
enemy_radius = 15
enemy_speed = 3

# Lista de enemigos
enemies = []

def create_enemy():
    enemy_x = random.randint(0, WIDTH)
    enemy_y = random.randint(0, HEIGHT)
    enemies.append([enemy_x, enemy_y])

# Añadir un enemigo cada cierto tiempo
pygame.time.set_timer(pygame.USEREVENT, 2000)  # Añadir un enemigo cada 2 segundos

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            create_enemy()

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
    window.fill(BLACK)
    pygame.draw.circle(window, player_color, (player_x, player_y), player_radius)

    for enemy in enemies:
        # Movimiento del enemigo hacia el jugador
        if enemy[0] < player_x:
            enemy[0] += enemy_speed
        if enemy[0] > player_x:
            enemy[0] -= enemy_speed
        if enemy[1] < player_y:
            enemy[1] += enemy_speed
        if enemy[1] > player_y:
            enemy[1] -= enemy_speed

        pygame.draw.circle(window, enemy_color, enemy, enemy_radius)

    pygame.display.update()
