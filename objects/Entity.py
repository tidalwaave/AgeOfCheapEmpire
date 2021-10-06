from ..CONSTANTS import *

class Entity:
	# https://ageofempires.fandom.com/wiki/Units_(Age_of_Empires) 
	# https://ageofempires.fandom.com/wiki/Buildings_(Age_of_Empires)
	def __init__(self, x, y, health, damage, rate_fire=1, range=0, melee_armor=0, pierce_armor=0, line_sight=4):
		self.x = x
		self.y = y
		self.health = health
		self.max_health = health
		self.damage = damage
		self.rate_fire = rate_fire
		self.range = range
		self.melee_armor = melee_armor
		self.pierce_armor = pierce_armor
		self.line_sight = line_sight

	# coordonnees
	def set_x(self, x):
		self.x = x

	def get_x(self):
		return self.x
	
	def set_y(self, y):
		self.y = y

	def get_y(self):
		return self.y

	# health
	def get_health(self):
		return self.health
	
	def set_health(self, health):
		self.health = health

	def gain_health(self, qty_health):
		self.health += qty_health
		if self.health > self.max_health:# on corrige le nb de pt de vie si celui-ci est superieur au maximum
			self.health = self.max_health
	
	def lose_health(self, qty_health):
		self.health -= qty_health
		if self.health < 0:# on corrige le nb de pt de vie si celui-ci est negatif
			self.health = 0
	
	def is_alive(self):
		return self.health > 0

	# max_health
	def get_max_health(self):
		return self.max_health

	def set_max_health(self, max_health):
		self.max_health = max_health

	# damage
	def get_damage(self):
		return self.damage
	
	def set_damage(self, damage):
		self.damage = damage
	
	# rate_fire
	def get_rate_fire(self):
		return self.rate_fire
	
	def set_rate_fire(self, rate_fire):
		self.rate_fire = rate_fire
	
	# range
	def get_range(self):
		return self.range
	
	def set_range(self, range):
		self.range = range

	# melee_armor
	def get_melee_armor(self):
		return self.melee_armor
	
	def set_melee_armor(self, melee_armor):
		self.melee_armor = melee_armor
	
	# pierce_armor
	def get_pierce_armor(self):
		return self.pierce_armor
	
	def set_pierce_armor(self, pierce_armor):
		self.pierce_armor = pierce_armor
	
	# line_sight
	def get_line_sight(self):
		return self.line_sight
	
	def set_line_sight(self, line_sight):
		self.line_sight = line_sight