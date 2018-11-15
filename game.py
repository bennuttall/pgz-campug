WIDTH = 1024
HEIGHT = 384

alien = Actor('alien')
alien.pos = (50, 320)
alien.jumping = False

def draw():
    screen.clear()
    alien.draw()

def update():
    if alien.y == 320 and keyboard[keys.UP] or alien.jumping:
        if alien.y > 100:
            alien.y -= 10
            alien.jumping = True
        else:
            alien.jumping = False
    elif alien.y < 320:
        alien.y += 10
    if keyboard[keys.LEFT] and alien.left > 0:
        alien.x -= 5
    if keyboard[keys.RIGHT] and alien.right < WIDTH:
        alien.x += 5