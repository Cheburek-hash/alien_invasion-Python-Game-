class Giveses():
	def ses(self):
		filename = open('stats.txt', 'r')
		with filename as f:
			save_early_stats = f.read()
		return save_early_stats
		
class Savescore():
	def __init__(self, stats, ses_2):
		
		self.stats = stats
		self.save_early_stats = ses_2.ses()
		self.high_score = float(self.save_early_stats)
	def save_high_score(self, stats):
		filename = open('stats.txt', 'r')
		with filename as f:
			self.save_early_stats = f.read()
		if float(self.save_early_stats) > self.high_score:
			print("Save stats bigger!")
			
			
		else:
			self.save_early_stats = str(self.high_score)
			filename = open('stats.txt', 'w')
			with filename as f:
				f.write(self.save_early_stats)
			
	
