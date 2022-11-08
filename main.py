import pgzrun
import random

TITLE = "lidia the coin collecter"
WIDTH = 1600
HEIGHT = 800

grass_color = (7, 195, 70)

lidia = Actor("lidia_south")
coin = Actor("coin")
lidia.center = (WIDTH / 2, HEIGHT / 2)
coin.center = (random.randrange(WIDTH), random.randrange(HEIGHT))
lidia_stepsize = 4


def draw():
    screen.clear()
    screen.fill(grass_color)
    coin.draw()
    lidia.draw()


def update():
    if keyboard.left:
        lidia.image = "lidia_west"
        lidia.x -= lidia_stepsize
    if keyboard.right:
        lidia.image = "lidia_east"
        lidia.x += lidia_stepsize
    if keyboard.up:
        lidia.image = "lidia_north"
        lidia.y -= lidia_stepsize
    if keyboard.down:
        lidia.image = "lidia_south"
        lidia.y += lidia_stepsize
    if coin.collidepoint((lidia.x, lidia.y)):
        coin.center = (random.randrange(WIDTH), random.randrange(HEIGHT))


pgzrun.go()
