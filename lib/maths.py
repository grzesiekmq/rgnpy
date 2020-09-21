import math
from random import random
class Maths():
	'''   convert radians to degrees
	
	@param angle
	@returns converted angle
	'''
	@staticmethod
	def rad_to_deg(angle):
		return angle * (180.0 / math.pi)
	

	'''   Gets random item from array.
	
	 @param array
	@returns The item.
	'''
	@staticmethod
	def random_item(array):
		max = len(array)
		index = round((random() * max))

		item = array[index]
		return item
	
