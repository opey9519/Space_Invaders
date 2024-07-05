import pygame as pg

pg.init()


HEIGHT = 600
WIDTH = 800

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Space Invaders')

BLACK = [0,0,0]

clock = pg.time.Clock()

run = True

while run:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

    clock.tick(30)

pg.quit()
