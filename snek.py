import pygame
import config
from stuff import Snake

pygame.init()
pygame.display.set_caption("Snek")
s = Snake(pos = [0,0])
while config.b.carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.b.carry_on = False

    s.move()
    config.b.draw()
    config.clock.tick(config.b.fps)


pygame.quit()

