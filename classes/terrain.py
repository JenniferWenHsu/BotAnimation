import matplotlib.pyplot as plt
import numpy as np
import random
import math

class Terrain: 
	""" 
	This constructs the Terrain for the environment. 
	The terrain is broken up to SEGCOUNT number of segments
	"""
	def __init__(self, 
				xlim = (0,100), 
				ylim = (0,1), 
				segCount = 10
				): 
		self.segCount = segCount
		self.segLength = (xlim[1] - xlim[0] + 1)/segCount
		self.xlim = xlim
		self.ylim = ylim 
		self.pointList = []
		for i in range(self.segCount): 
			# constructor of terrain is default to generate random terrain
			#self.pointList += [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
			self.pointList += [random.uniform(self.ylim[0], self.ylim[1])]

	# Plots only the terrain on screen 
	def drawTerrain(self): 
		fig = plt.figure()
		ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=self.xlim, ylim=(0,10))
		plt.plot(self.pointList)
		plt.show()

    # Obtain the corresponding Y value given a X value
	def getYValue(self, x): 
		x1 = int(math.floor(x/self.segLength))
		x2 = x1 + 1
		if x2 >= self.xlim[1]: 
			return self.pointList[self.xlim[1]]
		y1 = self.pointList[x1]
		y2 = self.pointList[x2]
		m = (float)(y2-y1)/(x2-x1)
		return y1 + m*(x-x1)

	# Obtain slope of the terrain given a X value
	def getSlope(self, x): 
		x1 = int(math.floor(x/self.segLength))
		x2 = x1 + 1
		if x1 == self.xlim[1]: 
			y1 = self.pointList[x1-1]
			y2 = self.pointList[x1]
		else: 
			y1 = self.pointList[x1]
			y2 = self.pointList[x2]
		return (float)(y2-y1)/(x2-x1)

	# Return a list of Y points
	def getPointList(self): 
		return self.pointList

	# Set pointList to determine the appearance of the terrain
	def setPointList(self, pointList): 
		self.pointList = pointList 
		self.segCount = len(pointList)
		
	# Return attribute xlim
	def getXLim(self): 
		return self.xlim

	# Return attribute ylim 
	def getYLim(self): 
		return self.ylim 
