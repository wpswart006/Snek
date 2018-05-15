from enum import Enum
import config
from tail import Tail

class DIRECTION(Enum):
	UP = 1
	RIGHT = 2
	DOWN = 3
	LEFT = 4

class Snake :
	speed = 55
	count = 0
	fps = 60
	hook = [2,3]
	direction = DIRECTION.RIGHT
	tail = []
	length = 0
	
	
	def __init__(self,pos,boardSize):
		self.pos = pos
		self.boardSize = boardSize

		
	def turnRight(self):
		if self.direction != DIRECTION.LEFT:
			self.direction = DIRECTION.RIGHT
			self.hurry()
		
	def turnLeft(self):
		# print("Turn Left")
		if self.direction != DIRECTION.RIGHT:
			self.direction = DIRECTION.LEFT
			self.hurry()

	def turnUp(self):
		# print(self.pos)
		# print(self.hook)
		# print(self.length)
		if self.direction != DIRECTION.DOWN:
			self.direction = DIRECTION.UP
			self.hurry()
		
	def turnDown(self):
		# print("Turn down")
		if self.direction != DIRECTION.UP:
			self.direction = DIRECTION.DOWN
			self.hurry()
		
	def move(self):
		self.count = self.count+1
		if self.count == self.fps+1-self.speed:
			self.hook = self.pos.copy()
			for k in range (self.length):
				self.tail[k].move()
			# print(hook)
			if self.direction == DIRECTION.RIGHT:
				# print(self.boardSize[0]-1)
				if self.pos[0] == self.boardSize[0]-1:
					# print("fg")
					self.pos[0] = 0
				else:
					self.pos[0] = self.pos[0]+1
			elif self.direction == DIRECTION.DOWN:
				if self.pos[1] == self.boardSize[1]-1:
					self.pos[1] =0
				else:
					self.pos[1] = self.pos[1]+1
			elif self.direction == DIRECTION.LEFT:
				if self.pos[0] == 0:
					self.pos[0] =self.boardSize[0]-1
				else:
					self.pos[0] = self.pos[0]-1
			elif self.direction == DIRECTION.UP:
				if self.pos[1] == 0:
					self.pos[1] =self.boardSize[0]-1
				else:
					self.pos[1] = self.pos[1]-1
			self.count =0
			# print("Done moving.")
			# print(self.hook)


	def hurry(self):
		self.count = self.fps-self.speed

	def grow(self):
		if self.length == 0:
			self.tail.append(Tail(self))
		else:
			# print(self.tail[self.length-1].pos)
			self.tail.append(Tail(self.tail[self.length-1]))
		self.length = self.length +1
		# print("Done growing.")
		
		# self.tail.append(Tail(self.tail[self.length-1].now,self.tail[self.length-1].next)


	