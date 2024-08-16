import random
from config import WIDTH, HEIGHT, ENEMY_COLOR, ENEMY_RADIUS, ENEMY_SPEED

def create_enemy():
    enemy_x = random.randint(0, WIDTH)
    enemy_y = random.randint(0, HEIGHT)
    return [enemy_x, enemy_y]


def move_enemy(enemy, player_x, player_y, speed):
    if abs(enemy[0] - player_x) > 1:  # Evitar movimientos si están muy cerca en el eje X
        if enemy[0] < player_x:
            enemy[0] += min(speed, player_x - enemy[0])
        elif enemy[0] > player_x:
            enemy[0] -= min(speed, enemy[0] - player_x)
    
    if abs(enemy[1] - player_y) > 1:  # Evitar movimientos si están muy cerca en el eje Y
        if enemy[1] < player_y:
            enemy[1] += min(speed, player_y - enemy[1])
        elif enemy[1] > player_y:
            enemy[1] -= min(speed, enemy[1] - player_y)
    
    return enemy




