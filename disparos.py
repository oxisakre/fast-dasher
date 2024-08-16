from config import BULLET_COLOR, BULLET_RADIUS, BULLET_SPEED

def shoot_bullet(x, y, direction):
    return [x, y, direction]

def move_bullet(bullet):
    if bullet[2] == 'up':
        bullet[1] -= BULLET_SPEED
    # Agregar otras direcciones si es necesario
    return bullet
