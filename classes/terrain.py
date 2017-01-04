import matplotlib.pyplot as plt
import numpy as np
import random 

import math
class Terrain: 
	# Contructor
	def __init__(self, 
				startPoint = 0.0, 
				endPoint = 10.0, 
				segCount = 10,
				xlim = (0,10), 
				ylim = (0,1) 
				): 
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.segCount = segCount
		self.segLength = (self.endPoint - self.startPoint)/segCount
		self.xlim = xlim
		self.ylim = ylim 
		self.pointList = []

	def drawTerrain(self): 
		fig = plt.figure()
		ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=self.xlim, ylim=(0,10))
		for i in range(self.segCount+1): 
			self.pointList += [random.uniform(self.ylim[0], self.ylim[1])]
		plt.plot(self.pointList)
		plt.show()

	def getYValue(self, x): 
		x1 = int(math.floor(x/self.segLength))
		x2 = int(math.ceil(x/self.segLength))
		
		y1 = self.pointList[x1]
		y2 = self.pointList[x2]
		m = (float)(y2-y1)/(x1-x2)
		return y1 + m*(x-x1)

	def getPointList(self): 
		for i in range(self.segCount+1): 
			self.pointList += [random.uniform(self.ylim[0], self.ylim[1])]
		return self.pointList
# testTerrain = Terrain()
# testTerrain.drawTerrain()

