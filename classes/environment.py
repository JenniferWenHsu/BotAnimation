import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import math

class Environment: 
	def __init__(self, mBot, mTerrain, 
				time_elapsed = 0, 
				bounds = [0, 9, -1, 10],
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
		self.bounds = bounds

	def timeStep(self, dt): 
		"""step once by dt seconds"""
		self.time_elapsed += dt

		# update positions
		vx = self.state[2]
		vy = self.state[3]
		self.state[0] = self.state[0] + dt*vx
		self.state[1] = self.state[1] + dt*vy

		# check for touching ground
		crossedTerrain = (self.state[1] <=
			self.terrain.getYValue(self.state[0]) + self.size)

		if crossedTerrain: 
			m = self.terrain.getSlope(self.state[0])
			# phi: slope angle
			phi = math.atan(m)
			# theta: angle between incoming vector plane normal vector
			if self.state[2] == 0: 
				self.state[2] = 0
				self.state[3] *= -1
				print("hit ground: ", self.state[3])
			else: 
				phi2 = math.atan(self.state[3]/self.state[2])
				theta = math.pi/2.0 - phi - phi2
				totalSpeed = math.sqrt(math.pow(self.state[2], 2)+math.pow(self.state[3], 2))
				self.state[2] = totalSpeed*math.cos(math.pi/2.0-theta+phi)
				self.state[3] = -1 * totalSpeed*math.sin(math.pi/2.0-theta+phi)

			self.state[1] = self.terrain.getYValue(self.state[0]) + self.size

		else: 
			crossed_x1 = (self.state[0] < self.bounds[0] + self.size)
			crossed_x2 = (self.state[0] > self.bounds[1] - self.size)
			crossed_y1 = (self.state[1] < self.bounds[2] + self.size)
			crossed_y2 = (self.state[1] > self.bounds[3] - self.size)

			if crossed_x1: 
				self.state[0] = self.bounds[0] + self.size
			if crossed_x2: 
				self.state[0] = self.bounds[1] - self.size
			if crossed_y1: 
				self.state[1] = self.bounds[2] + self.size
			if crossed_y2: 
				self.state[1] = self.bounds[3] - self.size
			# bouncing back 
			if crossed_x1 | crossed_x2: 
				self.state[2] *= -1
			if crossed_y1 | crossed_y2: 
				self.state[3] *= -1
			self.state[3] = self.state[3] - self.M * self.G * dt
		print("vy: ", self.state[3])

	def startAnimation(self): 
		# set up figure" 
		fig = plt.figure()
		fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
		ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, 
							xlim = (0, 9), ylim=(-1, 10))
		plt.plot(self.terrain.getPointList())
		particles, = ax.plot([], [], 'bo', ms=6)
		dt = 1./30

		def init(): 
			particles.set_data([], [])
			return particles, 

		def animate(i): 
			self.timeStep(dt)
			particles.set_data([self.state[0]], [self.state[1]])
			#print("state:", (self.state[0], self.state[1]))
			ms = int(fig.dpi * 2 * self.size * fig.get_figwidth() / np.diff(ax.get_xbound())[0])
			particles.set_markersize(ms)
			return particles,

		ani = animation.FuncAnimation(fig, animate, frames=600, interval=10, blit=True, init_func=init)

		plt.show()
