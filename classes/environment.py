import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

class Environment: 
	def __init__(self, mBot, mTerrain, 
				time_elapsed = 0, 
				size = 0.04,
				M = 1.0, 
				G = 9.8): 
		self.bot = mBot
		self.terrain = mTerrain
		self.time_elapsed = time_elapsed
		self.M = M
		self.G = G
		self.state = self.bot.getState()
		self.size = size 

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
		fig = plt.figure()
		fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
		ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, 
							xlim = (0, 10), ylim=(-1, 7))
		plt.plot(self.terrain.getPointList())
		particles, = ax.plot([], [], 'bo', ms=6)
		dt = 1./30

		def init(): 
			particles.set_data([], [])
			return particles, 

		def animate(i): 
			self.timeStep(dt)
			particles.set_data(self.state[0], self.state[1])
			ms = int(fig.dpi * 2 * self.size * fig.get_figwidth() / np.diff(ax.get_xbound())[0])
			particles.set_markersize(ms)
			return particles,

		ani = animation.FuncAnimation(fig, animate, frames=600, interval=10, blit=True, init_func=init)

		plt.show()
