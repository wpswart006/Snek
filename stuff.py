import numpy as np
import config
import pygame
import random
import numpy as np
from enum import Enum

class Board():

    def __init__(self,shape, block_size = 100):

<<<<<<< HEAD
||||||| merged common ancestors
<<<<<<<<< Temporary merge branch 1
        self.block_size = 10
||||||||| merged common ancestors
        self.block_size = 100
=========
=======

>>>>>>> 4211f9b895351a2a146d3a86dcb4c69dcb581ee2
        self.block_size = block_size
<<<<<<< HEAD
        self.block_size = 100
||||||| merged common ancestors
>>>>>>>>> Temporary merge branch 2
=======
>>>>>>> 4211f9b895351a2a146d3a86dcb4c69dcb581ee2
        self.shape= shape
        self.tiles = np.zeros((shape[1],shape[0]))
        self.tiles[2,2] = 1 
        self.size = (self.block_size*self.shape[1],self.block_size*self.shape[0])
        self.screen = pygame.display.set_mode(self.size)
        self.carry_on = True
        self.fps = 60
        self.wall = []
    
    def add_walls(self,wall):   
        for w in wall:
            self.wall.append(Wall(w))

            
    def draw(self):
        self.screen.fill([0,0,0])

        for x in range(self.shape[1]):
            for y in range(self.shape[0]):
                if self.tiles[x,y]== 1:
                    pygame.draw.rect(self.screen, [0,255,0], [x*self.block_size,y*self.block_size,self.block_size,self.block_size],0)
                elif self.tiles[x,y]== 2:
                    pygame.draw.rect(self.screen, [7,165,255], [x*self.block_size,y*self.block_size,self.block_size,self.block_size],0)
                elif self.tiles[x,y] == 3:
                    pygame.draw.rect(self.screen, [255,0,0], [x*self.block_size,y*self.block_size,self.block_size,self.block_size],0)
                elif self.tiles[x,y] == 4:
                    pygame.draw.rect(self.screen, [255,255,255], [x*self.block_size,y*self.block_size,self.block_size,self.block_size],0)
        pygame.display.flip()

class DIRECTION(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Snake():

    def __init__(self,pos = [3,3],snake_speed = 55):
        self.speed = snake_speed
        self.count = 0
        self.hook = [2,3]
        self.direction = DIRECTION.RIGHT
        self.tail = []
        self.length = 0
        self.pos = pos
        self.turn_allowed = True
        

    def move(self):
        if self.count == config.b.fps -self.speed:
            self.count = 0
            self.hook = self.pos.copy()
            if self.direction == DIRECTION.RIGHT:
                if self.pos[1] == config.b.shape[1] -1:
                    self.pos[1] = 0
                else:
                    self.pos[1] +=1
            elif self.direction == DIRECTION.UP:
                if self.pos[0] == 0:
                    self.pos[0] = config.b.shape[0]-1
                else:
                    self.pos[0] -=1
            elif self.direction == DIRECTION.LEFT:
                if self.pos[1] == 0:
                    self.pos[1] = config.b.shape[1]-1
                else:
                    self.pos[1] -=1
            elif self.direction == DIRECTION.DOWN:
                if self.pos[0] == config.b.shape[0]-1:
                    self.pos[0] = 0
                else:
                    self.pos[0] +=1
            config.b.tiles[self.hook[1],self.hook[0]] = 0
            config.b.tiles[self.pos[1],self.pos[0]] = 1
            for t in self.tail:
                t.move()
            if self.pos == config.f.pos:
                self.grow()
                config.f = Food()


        self.count +=1
        for t in self.tail:
            if self.pos == t.pos:
                self.die()
        for w in config.b.wall:
            if self.pos == w.pos:
                self.die()
        self.turn_allowed = True

    def turn_up(self):
        if self.turn_allowed and self.direction != DIRECTION.DOWN:
            self.turn_allowed = False
            self.direction = DIRECTION.UP
            self.hurry()
        
    def turn_down(self):
        if self.turn_allowed and self.direction != DIRECTION.UP:
            self.turn_allowed = False
            self.direction = DIRECTION.DOWN
            self.hurry()

    def turn_right(self):
        if self.turn_allowed and self.direction != DIRECTION.LEFT:
            self.turn_allowed = False
            self.direction = DIRECTION.RIGHT
            self.hurry()

    def turn_left(self):
        if self.turn_allowed and self.direction != DIRECTION.RIGHT:
            self.turn_allowed = False
            self.direction = DIRECTION.LEFT
            self.hurry()

    def hurry(self,amount = 0):
        self.count = config.b.fps -self.speed - amount

    def die(self):
        print(self.length)
        config.b.carry_on = False

    def grow(self):
        if self.length == 0:
            self.tail.append(Tail(self))
        else:
            self.tail.append(Tail(self.tail[self.length-1]))
            # print(self.tail[self.length-1])
        self.length +=1
            
class Tail():

    hook = [None,None]

    def __init__(self,parent):
        self.parent = parent
        self.pos = parent.hook.copy()

    def move(self):
        self.hook = self.pos.copy()
        self.pos = self.parent.hook.copy()

        if  config.b.tiles[self.hook[1],self.hook[0]] ==2:
            config.b.tiles[self.hook[1],self.hook[0]] = 0
        config.b.tiles[self.pos[1],self.pos[0]] = 2

class Food():

    def __init__(self):
        # print( config.b.tiles)
        avail = np.where(config.b.tiles == 0)
        # print(avail)
        x =random.randint(1,avail[0].size)-1
        # y = random.randint(1,avail[1].size)-1 SODAT JY KAN LEER UIT JOU FOUTE
        self.pos = [avail[1][x],avail[0][x]]
        config.b.tiles[self.pos[1],self.pos[0]] = 3
        # print(self.pos)
        # print( config.b.tiles)
        # print("\n")

class Wall():
    
    def __init__(self,pos):
        self.pos = pos
        config.b.tiles[self.pos[1],self.pos[0]] = 4