from paddle import Paddle
from ball import Ball
from enum import Enum
import random
class AI:
	Difficulty = Enum('Difficulty', ['EASY', 'MEDIUM', 'HARD', 'IMPOSSIBLE'])

	striker: Paddle
	ball: Ball
	height: float
	difficulty: Difficulty
	is_active: bool

	def __init__(self, striker, ball, difficulty):
		self.striker = striker
		self.ball = ball
		self.height = striker.height
		self.difficulty = difficulty
		self.random_error = 0
		self.is_active = True

	#movement for the ai paddle
	def move(self, ball, random_error):
		if ball.posy < (self.striker.posy + random_error):
			return -1
		elif ball.posy > (self.striker.posy + self.height + random_error):
			return 1
		else:
			return 0

	def update(self):
		if self.is_active:
			#print(f"Error: {self.random_error}")
			if self.difficulty == 'EASY':
				self.random_error = self.__clamp(self.random_error + random.randint(-3, 3), -20, 20)
			elif self.difficulty == 'MEDIUM':
				self.random_error = self.__clamp(self.random_error + random.randint(-2, 2), -15, 15)
			elif self.difficulty == 'HARD':
				self.random_error = self.__clamp(self.random_error + random.randint(-1, 1), -10, 10)
			else:
				# self.difficulty == 'IMPOSSIBLE', so there is no error
				pass
			YFac = self.move(self.ball, self.random_error)
			self.striker.update(YFac)
	
	def reset(self):
		self.random_error = 0
	
	#handles the random error value and clampes it at a certain amount
	def __clamp(self, n, min, max):
		if n < min:
			return min
		elif n > max:
			return max
		else:
			return n
