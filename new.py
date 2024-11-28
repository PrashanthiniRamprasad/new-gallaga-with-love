import pgzrun

WIDTH = 1400
HEIGHT = 700
ship = Actor("ship")
bug = Actor("bug")
speed = 5
ship.pos = (WIDTH / 2, HEIGHT - 50)

enemies = []
hearts = []

for x in range(10):
    for y in range(3):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y

score = 0
direction = 1
ship.dead = False
ship.countdown = 90
power_up_active = False

def displayScore():
    screen.draw.text(f"Score: {score}", (50, 30), fontsize=40)

def gameover():
    screen.draw.text("Game Over", (WIDTH // 3, HEIGHT // 3), fontsize=50)

def on_key_down(key):
    if ship.dead is False:
        if key == keys.SPACE:  # Shoot bullet when SPACE is pressed
            bullet = Actor("heart")
            bullet.x = ship.x
            bullet.y = ship.y - 20  # Place it above the ship
            bullets.append(heart)

def update():
    global score
    global direction
    move_down = False

    if ship.dead is False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH

    # Move bullets upwards
    for heart in hearts[:]:
        heart.y -= 10  # Bullet moves upward
        if heart.y < 0:  # Remove bullet if it goes off screen
            hearts.remove(heart)

        for enemy in enemies[:]:
            if heart.colliderect(enemy):  # Bullet hits enemy
                score += 100
                enemies.remove(enemy)
                hearts.remove(heart)
                break  # Stop checking other enemies once the bullet hits one

    # Handle enemies
    for heart in hearts:
        if heart.y <= 0:
            hearts.remove(heart)
        else:
            heart.y -= 10

    if len(enemies) == 0:
        gameover()

    if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x > 80):
        move_down = True
        direction = direction * -1

    for enemy in enemies:
        enemy.x += 5 * direction
        if move_down:
            enemy.y += 0.5
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

        if enemy.colliderect(ship):
            ship.dead = True

    if ship.dead:
        ship.countdown -= 1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90

def draw():
    screen.clear()
    screen.fill("black")

    for enemy in enemies:
        enemy.draw()

    for heart in hearts:
        heart.draw()  # Draw the bullets

    if ship.dead is False:
        ship.draw()

    displayScore()

    if len(enemies) == 0:
        gameover()

pgzrun.go()# Write your code here :-)
