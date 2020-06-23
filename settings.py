#settings game
import pygame
class Settings():
	#Parameters
	def __init__(self):
		#standart settings
		self.screen_width = 1000
		self.screen_height = 700
		self.bg_color =  (230, 230, 230)
		self.bg_image = pygame.image.load('img/bg.png')
		#settings of ship
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		#settings of bullet
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
		#settings aliens
		self.alien_speed_factor = 1
		self.aliens_move = False
		self.fleet_drop_speed = 10
		#fleet_derection (1 - right, -1 - left)
		self.fleet_direction = 1
		#speed game
		self.speedup_scale = 1.1
		#music settings
		self.music = 'res/hollywood-undead.ogg'
		self.sound_1 = 'your music'
		self.sound_2 = 'your music'
		self.sound_3 = 'your music'
		#standart volume
		self.volume = 0.5
		#init DS
		self.initialize_dynamic_settings()

		

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		#fleet_derection (1 - right, -1 - left)
		self.fleet_direction = 1
		#increase score
		self.alien_points = 50
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points *= 1.5
	def increase_standart_volume(self):
		self.volume += 0.10
	def decrease_standart_volume(self):
		self.volume -= 0.10

