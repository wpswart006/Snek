import config
from food import Food
from snake import Snake
import pygame


pygame.init()
# config.b.tiles[3,:] =1
# config.b.tiles[:,3] = 1
size = (20*config.b.shape[0],20*config.b.shape[1])
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

carryOn = True
clock = pygame.time.Clock()

s = Snake([2,2],[25,25])
f = Food()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.event.clear()
                s.turnLeft()
            elif event.key == pygame.K_RIGHT:
                pygame.event.clear()
                s.turnRight()
            elif event.key == pygame.K_UP:
                pygame.event.clear()
                s.turnUp()
            elif event.key == pygame.K_DOWN:
                pygame.event.clear()
                s.turnDown()
    
    screen.fill([0,0,0])
    s.move()
    config.b.update(s,f)
    config.b.draw(screen)
    pygame.display.flip()
    clock.tick(s.fps)

pygame.quit()

