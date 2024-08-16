import pygame
import sys
from ventana import iniciar_ventana
from enemigos import create_enemy, move_enemy
from disparos import shoot_bullet, move_bullet
from config import *
def main():
    window = iniciar_ventana()
    player_x = WIDTH // 2
    player_y = HEIGHT // 2
    bullets = []
    enemies = []

    pygame.time.set_timer(pygame.USEREVENT, 2000)  # Crear enemigos cada 2 segundos

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                enemies.append(create_enemy())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(shoot_bullet(player_x, player_y, 'up'))

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            player_y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            player_y += PLAYER_SPEED
        

        # Actualizar balas
        bullets = [move_bullet(bullet) for bullet in bullets]

        # Actualizar enemigos
        enemies = [move_enemy(enemy, player_x, player_y, ENEMY_SPEED) for enemy in enemies]

        # Dibujar todo
        window.fill((0, 0, 0))  # Pintar la pantalla de negro
        pygame.draw.circle(window, PLAYER_COLOR, (player_x, player_y), PLAYER_RADIUS)
        
        for enemy in enemies:
            pygame.draw.circle(window, ENEMY_COLOR, enemy, ENEMY_RADIUS)
        
        for bullet in bullets:
            pygame.draw.circle(window, BULLET_COLOR, (bullet[0], bullet[1]), BULLET_RADIUS)
        
        pygame.display.update()

if __name__ == "__main__":
    main()
