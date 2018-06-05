import pygame
from stuff import Snake,Board,Food


class Game():
    def __init__(self,display = True):
        self.walls = [[0,0],[0,1],[0,2],[0,3]]
        self.b = Board([10,10],block_size= 50)
        self.snake_speed = 55
        self.s = Snake(self.b,pos = [2,2],snake_speed= self.snake_speed)
        # self.f = None
        self.clock = pygame.time.Clock()
        
        self.start(display)

    def start(self,display):
        pygame.display.set_caption("Snek")
        # self.f = Food(self.b.tiles)
        while self.b.carry_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.b.carry_on = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.s.turn_up()
                    elif event.key == pygame.K_RIGHT:
                        self.s.turn_right()
                    elif event.key == pygame.K_DOWN:
                        self.s.turn_down()
                    elif event.key == pygame.K_LEFT:
                        self.s.turn_left()
            self.s.move()
            if display:
                self.b.draw()
                self.clock.tick(self.b.fps)
        self.stop()

    def stop(self):
        pygame.quit()
