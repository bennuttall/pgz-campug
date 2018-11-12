WIDTH = 1024
HEIGHT = 384

alien = Actor('alien')
alien.pos = (50, 320)

def draw():
    screen.clear()
    alien.draw()

def update():
    if keyboard[keys.UP]:
        if alien.y > 200:
            alien.y -= 2
    elif alien.y < 320:
        alien.y += 3
    if keyboard[keys.LEFT] and alien.left > 0:
        alien.x -= 2
    if keyboard[keys.RIGHT] and alien.right < WIDTH:
        alien.x += 2
    
