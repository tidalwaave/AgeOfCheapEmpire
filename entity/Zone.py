from entity.Entity import Entity
from utils.SpriteData import SpriteData
from utils.isometric import grid_pos_to_iso, TILE_HEIGHT
from CONSTANTS import Resource as Res

from LAUNCH_SETUP import LAUNCH_FAST_BUILD

# ----- GENERAL CLASS -----
class Zone(Entity):
	def __init__(self, grid_position, tile_size=(1, 1), is_locking=False, **kwargs):#constructeur : initialise les attributs
		iso_position = grid_pos_to_iso(grid_position)
		super().__init__(iso_position, **kwargs)
		self.grid_position=grid_position
		self.tile_size=tile_size
		self.is_locking = is_locking

	def get_grid_position(self):
		return self.grid_position

		# self.sprite = ZoneSprite(self, sprite_image, 1, center_x=iso_coords.x, center_y=iso_coords.y + 253//2 - TILE_HEIGHT, hit_box_algorithm="None")

# -------------------------

# Zone : Base brick of something that is present on the map, and not IN the map
#        Has a position, appears and disappears from the map
#
#
# Subclasses of Zone :
# Buildable : Civil, Military, Economic (no subclass & no need to differenciate)
# Resources (Natural !) : Mines, trees,
# Between both : buildable resources (champs)

# Tasklist :
# Town Center
# Buisson cueillette





#FILE NAMING CONVENTION : Zone_Buildable_TownCenter.py IN SUBFOLDERS ????


#   ____        _ _     _       _     _
#  |  _ \      (_) |   | |     | |   | |
#  | |_) |_   _ _| | __| | __ _| |__ | | ___
#  |  _ <| | | | | |/ _` |/ _` | '_ \| |/ _ \
#  | |_) | |_| | | | (_| | (_| | |_) | |  __/
#  |____/ \__,_|_|_|\__,_|\__,_|_.__/|_|\___|

# ----- GENERAL CLASS -----

class Buildable(Zone):
	def __init__(self, grid_position, cost=0, build_time=0, **kwargs):
		super().__init__(grid_position, **kwargs) # Calls parent class constructor
		self.cost = cost
		self.build_time = build_time

# -------------------------

# intégrer préconditions de construction de bat dans bat qui permet de construire bat
# avancées tech : fonction boucle faisant appel aux fonctions des objets respectifs pour modif leur propriétés

class WorkSite(Zone):
	# == In progess building, Not Implemented Yet.
	def __init__(self, grid_position, zone_to_build, **kwargs):
		super().__init__(grid_position, **kwargs)
		self.zone_to_build = zone_to_build


#
##
### Town Center
##
#
class TownCenter(Buildable):
	#WhoAmI : Cost : 200Wood 60sec build time
	#Size: 3x3
	#LineOfSight : 7
	#Equiv AOE2: TownCenter
	def __init__(self, grid_position):
		super().__init__(grid_position,
		sprite_data=SpriteData("Ressources/img/zones/buildables/towncenter.png", scale=1, y_offset=253//2 - TILE_HEIGHT),
		health=600,
		cost=(Res.WOOD, 200),
		build_time=2 if LAUNCH_FAST_BUILD else 60,
		tile_size=(3,3),
		line_sight=7)

class Barracks(Buildable):
		#WhoAmI : Cost : 125Wood and 30sec buildtime; Train & Upgrade infantry (Clubman)
		#Equiv AOE2: Barracks
	def __init__(self, grid_position):
		super().__init__(grid_position,
		sprite_data=SpriteData("Ressources/img/zones/buildables/barracks.png", scale=0.7, y_offset=255//2 - TILE_HEIGHT - 20),
		health=350,
		cost=(Res.WOOD, 125),
		build_time=2 if LAUNCH_FAST_BUILD else 30,
		tile_size=(3, 3))

class StoragePit(Buildable):
		#WhoAmI : Cost : 120 Wood, 30sec Build time; Use : Drop off wood, stone,gold (& food from hunt & fishing ONLY)
		#Size : 3x3
		#LineOfSight:4
		#Equiv AOE2: Lumber Camp & Mining Camp
	def __init__(self, grid_position):
		super().__init__(grid_position,
		sprite_data=SpriteData("Ressources/img/zones/buildables/storagepit.png", scale=0.7, y_offset=101//2 - 10),
		health=350,
		cost=(Res.WOOD, 120),
		build_time=2 if LAUNCH_FAST_BUILD else 30,
		tile_size=(2, 2)) # (3, 3) sur AOE, (2, 2) sur AOE2

class Granary(Buildable):
		#WhoAmI : Cost : 120 Wood, 30 sec build time; Use : Drop off Food from Gatherers, Foragers & Farmers (subclass Villager)
		#Equiv AOE2: Mill
	def __init__(self, grid_position):
		super().__init__(grid_position,
		sprite_data=SpriteData("Ressources/img/zones/buildables/granary.png", scale=0.7, y_offset=208//2 - TILE_HEIGHT - 15),
		health=350,
		cost=(Res.WOOD, 120),
		build_time=2 if LAUNCH_FAST_BUILD else 30,
		tile_size=(2, 2))


class Dock(Buildable):
		#WhoAmI : Cost : 100 Wood; Use : Train & upgrade ships
		#Equiv AOE2: Dock
	def __init__(self, grid_position):
		super().__init__(grid_position,
		sprite_data=SpriteData("Ressources/img/zones/buildables/dock.png", scale=0.7, y_offset=177//2 - 10),
		health=600,
		cost=(Res.WOOD, 100),
		build_time=2 if LAUNCH_FAST_BUILD else 35,
		tile_size=(3, 3))

class House(Buildable):
		#WhoAmI : Cost : 30 Wood; Use : +4 population per house
		#Equiv AOE2: House
	def __init__(self, grid_position):
		super().__init__(grid_position,
		sprite_data=SpriteData("Ressources/img/zones/buildables/house.png", scale=0.7, y_offset=126//2 - 10),
		health=75,
		cost=(Res.WOOD, 30),
		build_time=2 if LAUNCH_FAST_BUILD else 25,
		tile_size=(2, 2))



#  ______
#  | ___ \
#  | |_/ /  ___  ___   ___   _   _  _ __   ___   ___  ___
#  |    /  / _ \/ __| / _ \ | | | || '__| / __| / _ \/ __|
#  | |\ \ |  __/\__ \| (_) || |_| || |   | (__ |  __/\__ \
#  \_| \_| \___||___/ \___/  \__,_||_|    \___| \___||___/
#
#

# ----- GENERAL CLASS -----

class Resources(Zone):
	def __init__(self, grid_position, amount, **kwargs):
		super().__init__(grid_position, **kwargs) # Calls parent class constructor
		self.amount = amount
		self.max_amount = self.amount

	def __getstate__(self):
		return [self.get_grid_position(), self.is_locking, self.sprite_data, self.health, self.amount, self.max_amount]
	def __setstate__(self, data):
		super().__init__(data[0])
		self.is_locking=data[1]
		self.sprite_data=data[2]
		self.health = data[3]
		self.amount=data[4]
		self.max_amount=data[5]

	def get_resource_nbr(self):
		name = type(self).__name__.upper()
		enum_name = name if name != "BERRYBUSH" else "FOOD"
		return Res[enum_name]

	def harvest(self, dmg):
		if self.health > 0:
			self.health -= dmg
			return 0
		else:
			if self.amount > 0:
				self.amount -= 1
				return 1
			else:
				return -1


# -------------------------


class Wood(Resources):
	def __init__(self, grid_position):
		super().__init__(grid_position,
		sprite_data=SpriteData("Ressources/img/zones/resources/tree.png", scale=1, x_offset=-5, y_offset=187//2 - TILE_HEIGHT//2 + 5),
		health=25,
		amount=10)

class Stone(Resources):
	def __init__(self, grid_position):
		super().__init__(grid_position,
		is_locking=True,
		sprite_data=SpriteData("Ressources/img/zones/resources/stonemine.png", scale=1, y_offset=50//2 - TILE_HEIGHT//2),
		health=0,
		amount=250)

class Gold(Resources):
	def __init__(self, grid_position):
		super().__init__(grid_position,
		is_locking=True,
		sprite_data=SpriteData("Ressources/img/zones/resources/goldmine.png", scale=1, y_offset=50//2 - TILE_HEIGHT//2),
		health=0,
		amount=450)

class BerryBush(Resources):
	def __init__(self, grid_position):
		super().__init__(grid_position,
		is_locking=True,
		sprite_data=SpriteData("Ressources/img/zones/resources/berrybush.png", scale=1, y_offset=63//2 - TILE_HEIGHT//2),
		health=0,
		amount=150)