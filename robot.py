import math

class Robot_Movement:
	''' Here in the class Robot_Movement
	all the directions are given a default values of 0'''
	def __init__(self):
		self.up = 0
		self.down = 0
		self.left = 0
		self.right = 0

	def move_up(self,units):
		self.up += units

	def move_down(self,units):
		self.down += units

	def move_right(self,units):
		self.right += units

	def move_left(self,units):
		self.left += units

	def final_position(self):
		''' taking x as x co-ordinate and similarly for y'''
		x = self.up - self.down
		y = self.right - self.left
		position = int(math.hypot(x,y))
		print(f"The position of the robot is \n{position}")

robo_move = Robot_Movement()
''' ch is a temperary variable for convience for using conditional statements
uts signifies the units the robot is moved'''
while True:
	
	ch = int(input("Where would you like to move the robot\n\
	1. UP\n\
	2.DOWN\n\
	3.RIGHT\n\
	4.LEFT\n\
	5.Position of robot\n"))

	if ch == 1:
		uts = int(input	("enetr the units to be moved\n"))
		robo_move.move_up(uts)

	elif ch == 2:
		uts = int(input	("enetr the units to be moved\n"))
		robo_move.move_down(uts)

	elif ch == 3:
		uts = int(input	("enetr the units to be moved\n"))
		robo_move.move_right(uts)

	elif ch == 4:
		uts = int(input	("enetr the units to be moved\n"))
		robo_move.move_left(uts)

	elif ch == 5:
		break

	 	
robo_move.final_position()


