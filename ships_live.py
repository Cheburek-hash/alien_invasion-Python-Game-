import pygame
from pygame.sprite import Sprite


class Shipss(Sprite):
	def __init__(self, ai_settings, screen):
		super(Shipss, self).__init__()
		
		#init ship and start position
		self.screen = screen
		self.ai_settings = ai_settings
		#load ship
		self.image = pygame.image.load('img/ships.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
	