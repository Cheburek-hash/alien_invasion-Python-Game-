import game_functions as gf
class GameStats():
	#Stats
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		
		
	def check_game_active(self):
		if self.game_active == False:
			self.ai_settings.aliens_move = False
		if self.game_active == True:
			self.ai_settings.aliens_move = True

		
	def reset_stats(self):
	 	#stats real time
	 	self.ship_left = self.ai_settings.ship_limit
	 	self.score = 0
	 	self.level = 1



