class Environment: 
	def __init__(self, mBot, mTerrain, 
				time_elapsed = 0, 
				M = 1.0, 
				G = 9.8): 
		self.bot = mBot
		self.terrain = mTerrain
		self.time_elapsed = time_elapsed
		self.M = M
		self.G = G
		self.state = self.bot.getState()

	def isTouch(self):
		value = self.terrain.getYValue()
		yPos = self.state[1]
		return value == yPos

	def timeStep(self, dt): 
		"""step once by dt seconds"""
		self.time_elapsed += dt
		# update positions
		vx = self.state[2]
		vy = self.state[3]
		self.state[0] = vx*self.state[0]
		self.state[1] = vy*self.state[1]

		# check for touching ground 
		if self.isTouch: 
			self.state[2] *= -1
			self.state[2] *= -1

		# add gravity
		self.state[3] -= self.M * self.G * dt

	def startAnimation(self): 
		# set up figure" 
		figt = plt.figure()
		ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, 
							xlim = (-3.2, 3.2), ylim=(-2.4, 2.4))
		self.terrain.drawTerrain()

		# def init(): 
		# 	"""initialize animation"""
		# def animate(i): 

