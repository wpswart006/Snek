import pygame
import config
from stuff import Snake


pygame.display.set_caption("Snek")
s = Snake(pos = [2,2],snake_speed= config.snake_speed)
while config.b.carry_on:
    for event in config.pygame.event.get():
        if event.type == config.pygame.QUIT:
            config.b.carry_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                s.turn_up()
            elif event.key == pygame.K_RIGHT:
                s.turn_right()
            elif event.key == pygame.K_DOWN:
                s.turn_down()
            elif event.key == pygame.K_LEFT:
                s.turn_left()

    s.move()
    config.b.draw()
    config.clock.tick(config.b.fps)

print(s.length)
pygame.quit()

