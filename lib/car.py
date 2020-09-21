import math
from lib.car_parts.differential import Differential
from lib.car_parts.clutch import Clutch
from lib.car_parts.gearbox import Gearbox
from lib.car_parts.suspension import Suspension

from enum import Enum
from lib.maths import Maths


class Car():

	def __init__(self):
		self.differential = Differential()
		self.clutch = Clutch()
		self.gearbox = Gearbox()
		self.suspension = Suspension()

	distance = 0
	speed = 0
	top_speed = 0
	handling = 0
	make = ""
	model = ""
	color = ""
	description = ""
	hp = 0
	weight = 0
	wheel_base = 0.0
	rear_track = 0.0
	turn_radius = 0.0
	wheel_radius = 0.0
	RPM = 0
	is_locked = True
	is_won = False
	is_used = False
	AI_mode = False
	fuel_consumption = 0.0
	tire_exploit = 0.0

	# car related types
	class DriveType(Enum):
	
		AWD= 1
		FWD= 2
		RWD= 3
	

	class TransmissionType(Enum): 
		MT= 1
		AT= 2

	

	class CarType(Enum): 
	 
		SPORTS,RACECAR,SUPERCAR,DRIFT,DRAG,RALLY,CONCEPT,HYPERCAR,TUNED =	range(1, 10)

	class RacingType(Enum): 
		GTR= 1
		F1= 2
		TOURING= 3
	

	class TireType(Enum): 

  		SPORT,SEMISLICK,SLICK,SUPERSOFT,SOFT,MEDIUM,HARD,DRY,WET,STREET,RALLY,DIRT,SNOW,SUMMER = 	range(1, 15)

	class Paint(Enum): 
		MATTE= 1
		CHROME= 2
		METALLIC= 3
		PEARL= 4
		SOLID= 5
	

	class SafetySystems(Enum): 
		ABS= 1
		ESP= 2
		TCS= 3
		ESC= 4
		ASR= 5
	

	class Price(Enum): 
		USD= 1
		EUR= 2
	

	class Wheels(Enum): 
		# front
		FR= 1

		FL= 2

		# rear
		RL= 3

		RR= 4
	

	class WheelColliders(Enum): 
		# front
		COLFR= 1

		COLFL= 2

		# rear
		COLRL= 3

		COLRR= 4
	

	

	''' 
	 left angle of ackermann steering in degrees
	 params in metres
	 @param  rear_track
	 @param wheel_base
	@param turn_radius
	
	 @returns angle
	''' 

	@staticmethod
	def ackermann_left(rear_track, wheel_base, turn_radius):
		left = math.atan(wheel_base / (turn_radius + rear_track / 2))
		return Maths.rad_to_deg(left)

	
	'''
	 right angle of ackermann steering in degrees
	@param rear_track
	@param wheel_base
	@param turn_radius
	@returns angle
	'''
	@staticmethod
	def ackermann_right(rear_track, wheel_base, turn_radius):
		right = math.atan(wheel_base / (turn_radius - rear_track / 2))
		return Maths.rad_to_deg(right)

	'''  Meters per second to kmh.

	@param speed
	@returns speed in kmh
	'''
	@staticmethod
	def mps_to_kmh(speed):
		return round(speed * 3.6)

	'''  Meters to km.

	@param distance
	@returns The km.
	'''
	@staticmethod
	def m_to_km(distance):
		return distance / 1000

	'''     Kmh to mph

	@param speed
	@returns speed in mph
	'''
	@staticmethod
	def kmh_to_mph(speed):
		return round(speed / 1.61)

	'''  Mph to kmh

	@param speed
	@returns speed in kmh
	'''
	@staticmethod
	def mph_to_kmh(speed):
		return round(speed * 1.61)

	def accelerate(self, engine_force):
		#  rb.AddForce(engine_force)
		pass

	def brake(self, brake_force):
		#   rb.AddForce(brake_force)
  		pass

	def steer_left(self, torque):
		#   rb.AddTorque(torque * -1)
		pass

	def steer_right(self, torque):
		#   rb.AddTorque(torque)
		pass