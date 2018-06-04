import pygame
from stuff import Snake,Board,Food


pygame.display.set_caption("Snek")

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

pygame.quit()


class Game():
    def __init__(self,display = True):
        self.walls = [[0,0],[0,1],[0,2],[0,3]]
        self.b = Board([10,10],block_size= 50)
        self.f = Food()
        self.snake_speed = 55
        self.s = Snake(pos = [2,2],snake_speed= self.snake_speed)

        start(display)

    def start(self):
        while self.b.carry_on:
        # self.pygame = pygame.init() not sure yet


