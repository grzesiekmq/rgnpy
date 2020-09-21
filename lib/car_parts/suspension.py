import math
class Suspension():
	distance = 0.0
	def __init__(self):
		self.spring = self.Spring()

	@staticmethod
	def spring_rate(mass, distance, no_of_wheels = 4):
		return round(mass / no_of_wheels * 2 * 9.81 / distance)
	

	def compression_distance(self, weight, gravity, spring_rate):
		return round(weight * gravity / spring_rate)
	

	def force(self, spring_rate, compression_distance, damper, contact_speed):
		return round(spring_rate * compression_distance + damper * contact_speed)
	


	class Spring():
		spring_force = 0
		damper = 0
		target_pos = .5
	