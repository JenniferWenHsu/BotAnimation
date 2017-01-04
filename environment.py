class Environment: 
	def __init__(self, 
				mBot, 
				mTerrain, 
				time_elapsed = 0): 
		self.bot = mBot
		self.terrain = mTerrain
		self.time_elapsed = time_elapsed

	def isTouch(self):
		value = self.terrain.getYValue()
		position = self.bot.getPos()
		return value == position

	def timeStep(self, dt): 
		"""step once by dt seconds"""
		self.time_elapsed += dt
		# update positions
		# check for touching ground 
		# add gravity
