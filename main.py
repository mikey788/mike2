import pgzrun

WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
alien.x = 0
alien.y = 50

background = Actor('background')

def draw():
    screen.clear()
    background.draw()
    alien.draw()

def update():
    pass

def on_key_down(key):
    if key == keys.RIGHT:
        alien.x = alien.x + 2
    elif key == keys.LEFT:
        alien.x = alien.x - 2
    
pgzrun.go()


