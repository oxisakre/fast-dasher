# Lista de balas
bullets = []

def shoot_bullet(x, y, direction):
    bullets.append([x, y, direction])

# Añadir la funcionalidad de disparo
bullet_color = (255, 255, 0)
bullet_speed = 10
bullet_radius = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            create_enemy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot_bullet(player_x, player_y, 'up')

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

    # Mover balas
    for bullet in bullets:
        if bullet[2] == 'up':
            bullet[1] -= bullet_speed
        # Puedes añadir más direcciones según lo necesites

    # Lógica del juego
    window.fill(BLACK)
    pygame.draw.circle(window, player_color, (player_x, player_y), player_radius)

    for enemy in enemies:
        if enemy[0] < player_x:
            enemy[0] += enemy_speed
        if enemy[0] > player_x:
            enemy[0] -= enemy_speed
        if enemy[1] < player_y:
            enemy[1] += enemy_speed
        if enemy[1] > player_y:
            enemy[1] -= enemy_speed

        pygame.draw.circle(window, enemy_color, enemy, enemy_radius)

    # Dibujar las balas
    for bullet in bullets:
        pygame.draw.circle(window, bullet_color, (bullet[0], bullet[1]), bullet_radius)

    pygame.display.update()
