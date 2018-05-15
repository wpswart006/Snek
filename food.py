import random
import time
import os
import config
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np
class Food:
    def __init__(self):
        avail = np.where(config.b.tiles ==0)
        x =random.randint(1,avail[0].size)-1
        y = random.randint(1,avail[1].size)-1
        self.pos = [avail[0][x],avail[1][y]]
        
        # print("Done spawning")
        # print(self.y,self.y)