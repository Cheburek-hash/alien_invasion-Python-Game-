import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	#class to controll bullets
	def __init__(self, ai_settings, screen, ship):
		#creates an object bullets in the current positions of the ship 
		super(Bullet, self).__init__()
		self.screen = screen
		#create bullet in (0, 0) and assign right position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		#position of bullets
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	def update(self):
	 	self.y -= self.speed_factor
	 	self.rect.y = self.y
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)