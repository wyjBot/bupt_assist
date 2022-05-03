"""
This is the main file of the RoutePlaner Algorithm.

The class Planer contains the position of the person, the goal building and the map.
The class RoutePlaner contains the main function of the algorithm.
"""

class Planer:
	""" This class contains the position of the person, the goal building and the map. """
	def __init__(self, x, y, goal, map):
		self.x = x
		self.y = y
		self.goal = goal
		self.map = map
	
	def get_x(self):
		""" Returns the x position of the person. """
		return self.x
	
	def get_y(self):
		""" Returns the y position of the person. """
		return self.y

	def get_goal(self):
		""" Returns the goal building. """
		return self.goal

	def get_map(self):
		""" Returns the map. """
		return self.map

	def set_x(self, x):
		""" Sets the x position of the person. """
		self.x = x

	def set_y(self, y):
		""" Sets the y position of the person. """
		self.y = y

	def set_goal(self, goal):
		""" Sets the goal building. """
		self.goal = goal

	def set_map(self, map):
		""" Sets the map. """
		self.map = map

	def get_position(self):
		""" Returns the position of the person. """
		return (self.x, self.y)
	
	def get_goal_position(self):
		""" Returns the position of the goal building. """
		return self.goal.get_position()
	
