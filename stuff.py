import numpy as np
import config
import pygame
from enum import Enum

class Board():

    def __init__(self,shape):

        self.block_size = 100
        self.shape= shape
        self.tiles = np.zeros((shape[1],shape[0]))
        self.size = (self.block_size*self.shape[0],self.block_size*self.shape[1])
        self.screen = pygame.display.set_mode(self.size)
        self.carry_on = True
        self.fps = 60


    def draw(self):
        self.screen.fill([0,0,0])

        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.tiles[x,y]== 1:
                    pygame.draw.rect(self.screen, [0,255,0], [x*self.block_size,y*self.block_size,self.block_size,self.block_size],0)
                elif self.tiles[x,y]== 2:
                    pygame.draw.rect(self.screen, [7,165,255], [x*self.block_size,y*self.block_size,self.block_size,self.block_size],0)
                elif self.tiles[x,y] == 3:
                    pygame.draw.rect(self.screen, [255,0,0], [x*self.block_size,y*self.block_size,self.block_size,self.block_size],0)
        config.clock.tick(self.fps)
        config.pygame.display.flip()

class DIRECTION(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Snake():

    def __init__(self,pos = [3,3]):
        self.speed = 60
        self.count = 0
        self.hook = [2,3]
        self.direction = DIRECTION.RIGHT
        self.tail = []
        self.length = 0
        self.pos = pos

    def move(self):
        if self.count == self.speed:
            self.count = 0
            self.hook = self.pos.copy()
            if self.direction == DIRECTION.RIGHT:
                self.pos[1] +=1

        config.b.tiles[self.hook[1],self.hook[0]] = 0
        config.b.tiles[self.pos[1],self.pos[0]] = 1
        self.count +=1
