import pygame
class Tail:

    hook = [None,None]

    def __init__(self,parent):
       self.parent = parent
       self.pos = parent.hook.copy()
    #    print(self.pos)

    def move(self):
        self.hook = self.pos.copy()
        self.pos = self.parent.hook.copy()
        