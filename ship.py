import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()
		
		#init ship and start position
		self.screen = screen
		self.ai_settings = ai_settings
		#load ship
		self.image = pygame.image.load('img/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#start position
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom - 10
		self.center = float(self.rect.centerx)
		#flag moving
		self.moving_right = False
		self.moving_left = False
	def center_ship(self):
		self.center = self.screen_rect.centerx
	def update(self):
		#update ship's position taking into account the contents :D
		if self.moving_right and self.rect.right < self.screen_rect.right - 3:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 3:
			self.center -= self.ai_settings.ship_speed_factor
		#update atribute rect
		self.rect.centerx = self.center

	def blitme(self):
		#draw ship
		self.screen.blit(self.image, self.rect)