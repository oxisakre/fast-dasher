import random
from config import WIDTH, HEIGHT, ENEMY_COLOR, ENEMY_RADIUS, ENEMY_SPEED

def create_enemy():
    enemy_x = random.randint(0, WIDTH)
    enemy_y = random.randint(0, HEIGHT)
    return [enemy_x, enemy_y]

def move_enemy(enemy, player_x, player_y):
    if enemy[0] < player_x:
        enemy[0] += ENEMY_SPEED
    if enemy[0] > player_x:
        enemy[0] -= ENEMY_SPEED
    if enemy[1] < player_y:
        enemy[1] += ENEMY_SPEED
    if enemy[1] > player_y:
        enemy[1] -= ENEMY_SPEED
    return enemy
