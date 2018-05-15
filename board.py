import os
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np
import pygame


class Board:
  
    def __init__(self,shape):
      self.shape = shape
      self.tiles = np.zeros(self.shape)
   
    def draw(self,screen):
      for x in range(self.shape[0]):
        for y in range(self.shape[1]):
          if self.tiles[x,y]== 1:
            pygame.draw.rect(screen, [0,255,0], [x*20,y*20,20,20],0)
          elif self.tiles[x,y]== 2:
            pygame.draw.rect(screen, [7,165,255], [x*20,y*20,20,20],0)
          elif self.tiles[x,y] == 3:
            pygame.draw.rect(screen, [255,0,0], [x*20,y*20,20,20],0)

    def update(self,snake,food):
      if(snake.pos == food.pos):
        snake.grow()
        with open ('out.txt', 'a') as f:
            print(snake.length,":\n",self.tiles,file = f)
        food.__init__()
          
      self.tiles = np.zeros(self.shape)
      
      # print("update")
      # print(snake.pos)
      self.tiles[food.pos[0],food.pos[1]] = 3
      for k in snake.tail:
        self.tiles[k.pos[0],k.pos[1]] = 2
      
      self.tiles[snake.pos[0],snake.pos[1]] =1
      # print("Done Updating")
      # print(np.where(self.tiles==3))
      
        





   
