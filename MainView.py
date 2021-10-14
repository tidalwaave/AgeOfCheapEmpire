# Imports
import arcade
import arcade.gui

import random

#############################################################
#					Custom buttons							#
#############################################################

# Button to exit the game
class QuitButton(arcade.gui.UIFlatButton):
	def on_click(self, event: arcade.gui.UIOnClickEvent):
		arcade.exit()

# Button to return to the main menu
class ReturnToMenuButton(arcade.gui.UIFlatButton):
	def __init__(self, window, text, width):
		super().__init__(text=text, width=width)
		self.window = window

	def on_click(self, event: arcade.gui.UIOnClickEvent):
		print("Retour :", event)
		main_view = MainView()
		self.window.show_view(main_view)


#############################################################
#						Main View							#
#############################################################

# View d'accueil : première à etre affichée à l'écran
class MainView(arcade.View) :
	def on_show(self):
		""" This is run once when we switch to this view """
		#arcade.set_background_color(arcade.csscolor.WHITE)

		# ajoute l'image de background
		self.texture = arcade.load_texture("./img/background.png")

		# a UIManager to handle the UI.
		self.manager = arcade.gui.UIManager()
		self.manager.enable()

		#on appel la fonction pour afficher les bouttons de bases
		self.create_buttons()


	def on_draw(self):
		""" Draw this view """
		arcade.start_render()
		self.texture.draw_sized(self.window.width / 2, self.window.height / 2, self.window.width, self.window.height)
		#arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
		#arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75, arcade.color.WHITE, font_size=20, anchor_x="center")
		self.manager.draw()

	def on_hide_view(self) :
		self.manager.disable()

	def on_click_start(self, event):
		print("Start:", event)
		""" If the user presses the mouse button, start the game. """
		game_view = GameView()
		game_view.setup()
		self.window.show_view(game_view)


	def create_buttons(self):
		# def button size
		buttonsize = self.window.width / 6

		# Create a vertical BoxGroup to align buttons
		self.v_box = arcade.gui.UIBoxLayout()

		# Create the buttons
		start_button = arcade.gui.UIFlatButton(text="Start Game", width=buttonsize)
		self.v_box.add(start_button.with_space_around(bottom=20))
		start_button.on_click = self.on_click_start # link the on_click method of the button with a fonction

		settings_button = arcade.gui.UIFlatButton(text="Settings", width=buttonsize)# OR SettingsButton(...) but idk the goal this class (but it can be change without any pb)
		self.v_box.add(settings_button.with_space_around(bottom=20))
		settings_button.on_click = self.on_click_settings # link the on_click method of the button with a fonction

		# Again, method 1. Use a child class to handle events.
		quit_button = QuitButton(text="Quit", width=buttonsize)
		self.v_box.add(quit_button)

		# Create a widget to hold the v_box widget, that will center the buttons
		self.manager.add(
			arcade.gui.UIAnchorWidget(
				anchor_x = "left",
				align_x = buttonsize,
				anchor_y="center_y",
				child=self.v_box
			)
		)

	def on_click_settings(self, event):
		print("Settings:", event)
		settings_view = SettingsView()
		self.window.show_view(settings_view)

#############################################################
#						Settings View						#
#############################################################

# View des paramètres accessible via ecran d'accueil
class SettingsView(arcade.View) :
	""" Settings view """

	def on_show(self):
		""" This is run once when we switch to this view """

		# a UIManager to handle the UI.
		self.manager = arcade.gui.UIManager()
		self.manager.enable()

		# ajoute l'image de background
		self.texture = arcade.load_texture("./img/background.png")

		self.create_buttons()

	def create_buttons(self) :
		# def sizes
		buttonsize = self.window.width / 6
		checkboxsize = buttonsize / 2
		# Create a vertical BoxGroup to align buttons
		self.v_box = arcade.gui.UIBoxLayout()

		# Create an UITextureButton
		texture = arcade.load_texture("img/tick.png")
		music_button = arcade.gui.UITextureButton(texture=texture, text="Musique", width=checkboxsize, height=checkboxsize)
		self.music = True

		# Handle Clicks
		@music_button.event("on_click")
		def on_click_music_button(event) :
			print("Music checkbox pressed", event)
			if self.music :
				event.source.texture = arcade.load_texture("img/blanc.png")
				self.music = False
			else :
				event.source.texture = arcade.load_texture("img/tick.png")
				self.music = True

		self.v_box.add(music_button.with_space_around(bottom=20))

		fullscreen_button = arcade.gui.UITextureButton(texture=texture, text="Plein écran", width=checkboxsize, height=checkboxsize)
		self.fullscreen = True

		# Handle Clicks
		@fullscreen_button.event("on_click")
		def on_click_fullscreen_button(event) :
			print("Fullscreen checkbox pressed", event)
			if self.fullscreen :
				event.source.texture = arcade.load_texture("img/blanc.png")
				self.fullscreen = False
			else :
				event.source.texture = arcade.load_texture("img/tick.png")
				self.fullscreen = True

		self.v_box.add(fullscreen_button.with_space_around(bottom=20))

		retour_button = ReturnToMenuButton(self.window, text="Retour", width=buttonsize)
		self.v_box.add(retour_button.with_space_around(bottom=20))

		# Create a widget to hold the v_box widget, that will center the buttons
		self.manager.add(
			arcade.gui.UIAnchorWidget(
				anchor_x = "left",
				align_x = buttonsize,
				anchor_y="center_y",
				child=self.v_box
			)
		)

	def on_draw(self):
		""" Draw this view """
		arcade.start_render()

		self.texture.draw_sized(self.window.width / 2, self.window.height / 2, self.window.width, self.window.height)
		arcade.draw_text("Settings Screen", self.window.width / 3, self.window.height * 4 / 6, arcade.color.WHITE, font_size=50, anchor_x="center")

		self.manager.draw()


	def on_click_music(self, event) :
		print("Music :", event)

	def on_hide_view(self) :
		self.manager.disable()

#############################################################
#					Fake Game								#
#############################################################

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Age Of Cheap Empire"

class GameView(arcade.View):
	""" Our custom Window Class"""

	def __init__(self):
		""" Initializer """
		# Call the parent class initializer
		super().__init__()

		# Variables that will hold sprite lists
		self.player_list = None
		self.coin_list = None

		# Set up the player info
		self.player_sprite = None
		self.score = 0

		# Don't show the mouse cursor
		self.window.set_mouse_visible(False)

		arcade.set_background_color(arcade.color.AMAZON)

	def setup(self):
		""" Set up the game and initialize the variables. """

		# Sprite lists
		self.player_list = arcade.SpriteList()
		self.coin_list = arcade.SpriteList()

		# Score
		self.score = 0

		# Set up the player
		# Character image from kenney.nl
		self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
		self.player_sprite.center_x = 50
		self.player_sprite.center_y = 50
		self.player_list.append(self.player_sprite)

		# Create the coins
		for i in range(COIN_COUNT):

			# Create the coin instance
			# Coin image from kenney.nl
			coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

			# Position the coin
			coin.center_x = random.randrange(SCREEN_WIDTH)
			coin.center_y = random.randrange(SCREEN_HEIGHT)

			# Add the coin to the lists
			self.coin_list.append(coin)

	def on_draw(self):
		""" Draw everything """
		arcade.start_render()
		self.coin_list.draw()
		self.player_list.draw()

		# Put the text on the screen.
		output = f"Score: {self.score}"
		arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

	def on_mouse_motion(self, x, y, dx, dy):
		""" Handle Mouse Motion """

		# Move the center of the player sprite to match the mouse x, y
		self.player_sprite.center_x = x
		self.player_sprite.center_y = y

	def on_update(self, delta_time):
		""" Movement and game logic """

		# Call update on all sprites (The sprites don't do much in this
		# example though.)
		self.coin_list.update()

		# Generate a list of all sprites that collided with the player.
		coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

		# Loop through each colliding sprite, remove it, and add to the score.
		for coin in coins_hit_list:
			coin.remove_from_sprite_lists()
			self.score += 1
